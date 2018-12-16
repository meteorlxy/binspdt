<template>
  <VCard>
    <VLayout
      class="py-2 px-3"
      row
      wrap>
      <VFlex xs6>
        <VBtn
          color="grey"
          title="Back To Modules List"
          :to="{ name: 'dashboard.modules' }"
          exact
          icon
          flat
          :disabled="hasPending">
          <VIcon>arrow_back</VIcon>
        </VBtn>

        <VBtn
          color="grey"
          title="Reset"
          flat
          icon
          :disabled="hasPending"
          @click="files = []">
          <VIcon>refresh</VIcon>
        </VBtn>
      </VFlex>

      <VFlex
        class="text-xs-right"
        xs6>
        <VBtn
          color="success"
          title="Start Upload"
          :icon="$vuetify.breakpoint.smAndDown"
          :loading="hasPending"
          :disabled="!hasPending && !hasUnstarted"
          @click="handlePostModules">
          <VIcon :left="!$vuetify.breakpoint.smAndDown">
            check
          </VIcon>

          <span class="hidden-sm-and-down">
            Start Upload
          </span>
        </VBtn>

        <VBtn
          color="primary"
          title="Add Files"
          :icon="$vuetify.breakpoint.smAndDown"
          :disabled="hasPending"
          @click="$refs.files.click()">
          <VIcon :left="!$vuetify.breakpoint.smAndDown">
            note_add
          </VIcon>

          <span class="hidden-sm-and-down">
            Add Files
          </span>
        </VBtn>

        <input
          v-show="false"
          ref="files"
          type="file"
          :accept="filesAccept"
          multiple
          @change="addFiles">
      </VFlex>

      <VFlex
        xs12
        md6>
        <VSelect
          v-model="idaVersion"
          class="mx-2 d-inline-block"
          label="IDA Pro Version"
          :items="idaVersionItems"/>

        <VTooltip
          v-show="!isBinaryFiles"
          top>
          <VIcon
            slot="activator"
            style="cursor: pointer">
            help_outline
          </VIcon>

          <span>Make sure to select the corresponding IDA Pro version of the .idb/.i64 files</span>
        </VTooltip>
      </VFlex>

      <VFlex
        class="text-md-right"
        xs12
        md6>
        <VRadioGroup
          v-model="isBinaryFiles"
          class="d-inline-block"
          row>
          <VRadio
            label="binary file"
            :value="true"
            disabled/>
          <VRadio
            label=".idb/.i64 file"
            :value="false"/>
        </VRadioGroup>
      </VFlex>
    </VLayout>

    <VDataTable
      :headers="tableHeaders"
      :items="tableItems"
      hide-actions>
      <template slot="no-data">
        <div class="text-xs-center">
          <VBtn
            flat
            title="Add Files"
            :disabled="hasPending"
            @click="$refs.files.click()">
            Add files to upload
          </VBtn>
        </div>
      </template>

      <template
        slot="items"
        slot-scope="props">
        <td>{{ props.index }}</td>

        <td>{{ props.item.file.name }}</td>

        <td>{{ $helpers.filesize(props.item.file.size) }}</td>

        <td>
          <VProgressLinear
            :color="getFileStatus(props.item).color"
            :value="props.item.percentage"/>
        </td>

        <td>
          <span :class="`${getFileStatus(props.item).color}--text`">
            {{ getFileStatus(props.item).text }}
          </span>
        </td>

        <td>
          <VBtn
            class="ml-0"
            :title="props.item.status === 2 ? 'Finish' : 'Remove this file'"
            icon
            small
            :disabled="props.item.status === 1"
            @click="removeFile(props.index)">
            <VIcon>{{ props.item.status === 2 ? 'check' : 'close' }}</VIcon>
          </VBtn>
        </td>
      </template>
    </VDataTable>
  </VCard>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'
import { namespace } from 'vuex-class'
import { requestCatch } from '@/utils/catchError'

type UploadFile = { status: number, percentage: number, file: File }

@Component
export default class ModulesUpload extends Vue {
  @namespace('binary/modules').Action('postModules') postModules

  files: Array<UploadFile> = []

  isBinaryFiles: Boolean = false

  idaVersion: String = '6.8'

  get idaVersionItems () {
    return [
      '6.8',
    ]
  }

  get filesAccept () {
    return this.isBinaryFiles ? '*' : '.idb,.i64'
  }

  get tableHeaders () {
    return [
      { text: '#', value: '' },
      { text: 'Name', value: 'name' },
      { text: 'Size', value: 'size', class: 'hidden-xs-only' },
      { text: 'Progress', value: '', sortable: false },
      { text: 'Status', value: '', sortable: false },
      { text: 'Actions', value: '', sortable: false },
    ]
  }

  get tableItems () {
    return this.files
  }

  get hasUnstarted () {
    return this.files.some(item => item.status <= 0)
  }

  get hasPending () {
    return this.files.some(item => item.status === 1)
  }

  beforeRouteLeave (to, from, next) {
    if (this.hasPending) {
      if (confirm('Uploading is in progress, confirm to leave?')) {
        next()
      }
    } else {
      next()
    }
  }

  addFiles (this: any) {
    const newFilesArr: Array<File> = Array.from(this.$refs.files.files)
    for (const newFile of newFilesArr) {
      // Check if the new file has already in the files list
      if (!this.files.find(item => {
        return item.file.name === newFile.name &&
          item.file.size === newFile.size &&
          item.file.lastModified === newFile.lastModified
      })
      ) {
        // If choose to upload .idb/.i64 files, check the file extension
        const newFileExt = newFile.name.split('.').pop() || ''
        if (!this.isBinaryFiles && !['idb', 'i64'].includes(newFileExt)) {
          continue
        }

        // Push the new file into the files list
        this.files.push({
          status: 0,
          percentage: 0,
          file: newFile,
        })
      }
    }

    // Reset the files in the <input> DOM
    this.$refs.files.value = ''
  }

  removeFile (index) {
    this.files.splice(index, 1)
  }

  getFileStatus (uploadFile) {
    if (uploadFile.status === -1) {
      return {
        color: 'red',
        text: 'Error',
      }
    } else if (uploadFile.status === 0) {
      return {
        color: 'grey',
        text: 'Wait',
      }
    } else if (uploadFile.status === 1 && uploadFile.percentage !== 100) {
      return {
        color: 'blue',
        text: 'Uploading',
      }
    } else if (uploadFile.status === 1 && uploadFile.percentage === 100) {
      return {
        color: 'purple',
        text: 'Importing',
      }
    } else {
      return {
        color: 'green',
        text: 'Success',
      }
    }
  }

  async handlePostModules () {
    // If there is no files to upload, or there are some files uploading, skip
    if (this.files.length === 0 || this.hasPending) {
      return false
    }

    try {
      const postPromiseAll: Array<any> = []

      for (const file of this.files) {
        // If the file has been uploaded, skip
        if (file.status > 0) {
          continue
        }

        // Set the status to 'uploading', and reset the percentage for those files with errors
        file.status = 1
        file.percentage = 0

        // Create the post file promise
        const postPromise = this.postModules({
          files: [file.file],
          version: this.idaVersion,
          onUploadProgress: (progress) => {
            // Watch the upload progress
            file.percentage = Math.floor((progress.loaded * 100) / progress.total)
          },
        }).then(res => {
          // Set the status to 'success' when uploaded
          file.status = 2
          return res
        }).catch(err => {
          // Set the status to 'error' when failed
          file.status = -1
          throw err
        })
        postPromiseAll.push(postPromise)
      }

      // Promise.all the upload process
      await Promise.all(postPromiseAll)

      // Show the notice
      this.$notify({
        type: 'success',
        title: 'Success',
        text: `Upload successfully.`,
      })
    } catch (error) {
      requestCatch(error)
    }
  }
}
</script>
