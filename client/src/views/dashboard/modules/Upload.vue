<template>
  <div class="col-12">
    <Card>
      <template slot="title">
        <FaIcon icon="upload"/>

        <span class="ml-1">Upload New Modules</span>
      </template>

      <CardBody
        slot="body"
        class="p-0">
        <input
          v-show="false"
          type="file"
          ref="files"
          accept=".idb,.i64"
          multiple
          @change="addFiles"/>

        <ATable
          v-if="files.length"
          hover
          striped>
          <thead>
            <tr>
              <th>#</th>

              <th>Name</th>

              <th>Size</th>

              <th>Action</th>
            </tr>
          </thead>

          <TransitionFadeSlide
            tag="tbody"
            direction="x"
            group>
            <tr
              v-for="(file, index) in files"
              :key="`${file.name}.${file.size}.${file.type}.${file.lastModified}`">
              <td>{{ index + 1 }}</td>

              <td>{{ file.name }}</td>

              <td>{{ $helpers.filesize(file.size) }}</td>

              <td>
                <button
                  class="btn btn-sm btn-danger rounded-circle"
                  title="Remove file"
                  @click="removeFile(index)">
                  <FaIcon icon="trash-alt"/>
                </button>
              </td>
            </tr>
          </TransitionFadeSlide>
        </ATable>
      </CardBody>

      <CardFooter slot="footer">
        <button
          class="btn btn-primary"
          @click="$refs.files.click()">
          <FaIcon icon="plus"/>

          <span class="ml-1">Add Files</span>
        </button>

        <button
          v-show="files.length"
          class="btn btn-default"
          @click="files = []">
          <FaIcon icon="redo-alt"/>

          <span class="ml-1">Reset</span>
        </button>

        <button
          class="btn btn-success float-right"
          :disabled="!files.length"
          @click="handleFilesUpload">
          <FaIcon icon="check"/>

          <span class="ml-1">Upload Files</span>
        </button>
      </CardFooter>
    </Card>
  </div>
</template>

<script>
import ATable from '@/components/admin-lte/ATable.vue'
import Card from '@/components/admin-lte/Card.vue'
import CardBody from '@/components/admin-lte/CardBody.vue'
import CardFooter from '@/components/admin-lte/CardFooter.vue'
import TransitionFadeSlide from '@/components/TransitionFadeSlide.vue'
import { mapActions } from 'vuex'

export default {
  name: 'DashboardModulesUpload',

  components: {
    ATable,
    Card,
    CardBody,
    CardFooter,
    TransitionFadeSlide,
  },

  data(){
    return {
      files: []
    }
  },

  methods: {
    ...mapActions('binary/modules', [
      'postModules',
    ]),
  
    addFiles () {
      const newFilesArr = Array.from(this.$refs.files.files)
      for (const newFile of newFilesArr) {
        if (!this.files.find(f => f.name === newFile.name && f.size === newFile.size && f.lastModified  === newFile.lastModified)) {
          this.files.push(newFile)
        }
      }
      this.$refs.files.value = ''
    },

    removeFile (index) {
      this.files.splice(index, 1)
    },

    async handleFilesUpload () {
      if (this.files.length < 1) {
        return false
      }

      try {
        await this.postModules({
          version: '6.8',
          files: this.files,
        })
      } catch (e) {

      } finally {

      }
    },
  }
}
</script>
