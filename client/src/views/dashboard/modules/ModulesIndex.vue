<template>
  <VCard>
    <VToolbar
      color="white"
      flat>
      <VToolbarTitle>
        <span>List of Modules</span>
      </VToolbarTitle>

      <VSpacer/>

      <VBtn
        color="primary"
        title="Upload New Modules"
        :to="{ name: 'dashboard.modules.upload' }"
        :icon="$vuetify.breakpoint.smAndDown">
        <VIcon :left="!$vuetify.breakpoint.smAndDown">
          backup
        </VIcon>

        <span class="hidden-sm-and-down">
          Upload New Modules
        </span>
      </VBtn>
    </VToolbar>

    <VToolbar
      color="white"
      flat>
      <VBtn
        color="grey"
        title="Refresh"
        flat
        icon
        :loading="isLoading"
        @click="handleRefresh">
        <VIcon>refresh</VIcon>
      </VBtn>

      <VMenu
        offset-y
        :disabled="tableSelected.length === 0 || isLoading">
        <template v-slot:activator>
          <VBtn
            color="indigo"
            title="Manipulate selected modules"
            flat
            round
            :icon="$vuetify.breakpoint.smAndDown"
            :disabled="tableSelected.length === 0 || isLoading">
            <VIcon :left="!$vuetify.breakpoint.smAndDown">
              check_box
            </VIcon>

            <span class="hidden-sm-and-down">
              Manipulate Selected
            </span>
          </VBtn>
        </template>

        <VList>
          <VListTile @click="handleDeleteModules">
            <VListTileAvatar>
              <VIcon>delete</VIcon>
            </VListTileAvatar>

            <VListTileTitle>
              Delete Selected Modules
            </VListTileTitle>
          </VListTile>
        </VList>
      </VMenu>

      <VSpacer/>

      <VTextField
        v-model="search"
        class="pt-0"
        type="text"
        label="Search"
        append-icon="search"
        clearable
        single-line
        hide-details
        :disabled="isLoading"
        @click:append="handleGetModules"
        @keydown.enter="handleGetModules"/>
    </VToolbar>

    <VDataTable
      v-model="tableSelected"
      :headers="tableHeaders"
      :items="tableItems"
      :total-items="tableItemsTotal"
      :loading="isLoading"
      :pagination.sync="tablePagination"
      :rows-per-page-items="[10, 25, 50]"
      select-all>
      <template v-slot:items="props">
        <td>
          <VCheckbox
            v-model="props.selected"
            primary
            hide-details/>
        </td>

        <td>{{ props.item.id }}</td>

        <td>{{ props.item.name }}</td>

        <td class="hidden-xs-only">
          {{ props.item.architecture }}
        </td>

        <td class="hidden-xs-only">
          {{ $helpers.formatDateTime(props.item.import_time) }}
        </td>

        <td class="hidden-sm-and-down">
          {{ props.item.md5 }}
        </td>

        <td>
          <VBtn
            class="ml-0"
            icon
            small
            color="primary"
            title="Inpect this module"
            :to="{ name: 'dashboard.modules.details', params: { id: props.item.id } }">
            <VIcon>search</VIcon>
          </VBtn>

          <VBtn
            class="ml-0"
            icon
            small
            color="error"
            title="Remove this module"
            @click="handleDeleteModule(props.item.id)">
            <VIcon>delete_outline</VIcon>
          </VBtn>
        </td>
      </template>
    </VDataTable>
  </VCard>
</template>

<script lang="ts">
import { Vue, Component, Watch } from 'vue-property-decorator'
import { namespace } from 'vuex-class'
import { requestCatch } from '@/utils/catchError'

@Component
export default class ModulesIndex extends Vue {
  @namespace('binary/modules').State('modules') modules
  @namespace('binary/modules').State('isLoading') isLoading
  @namespace('binary/modules').Action('getModules') getModules
  @namespace('binary/modules').Action('deleteModule') deleteModule
  @namespace('binary/modules').Action('deleteModules') deleteModules

  tablePagination: any = {
    page: this.$store.state.binary.modules.modules.page,
    rowsPerPage: 25,
    descending: true,
  }

  tableSelected: Array<any> = []

  search: string = ''

  get tableHeaders () {
    return [
      { text: '#', value: 'id' },
      { text: 'Name', value: 'name' },
      { text: 'Arch.', value: 'architecture', class: 'hidden-xs-only' },
      { text: 'Upload Time', value: 'import_time', class: 'hidden-xs-only' },
      { text: 'MD5', value: 'md5', class: 'hidden-sm-and-down' },
      { text: 'Actions', value: '', sortable: false },
    ]
  }

  get tableItems () {
    return this.modules.data
  }

  get tableItemsTotal () {
    return this.modules.count
  }

  @Watch('tablePagination', { deep: true })
  onTablePaginationChange (val: any) {
    this.handleGetModules()
  }

  created () {
    this.handleGetModules()
  }

  resetSelected () {
    this.tableSelected.splice(0, this.tableSelected.length)
  }

  async handleRefresh () {
    this.resetSelected()
    await this.handleGetModules()
  }

  async handleGetModules () {
    const { sortBy, descending, page, rowsPerPage } = this.tablePagination
    await this.getModules({
      page: page,
      perPage: rowsPerPage,
      orderBy: `${descending ? '-' : ''}${sortBy}`,
      search: this.search,
    })
  }

  async handleDeleteModule (id) {
    if (!confirm(`Confirm to delete module #${id} ?`)) {
      return false
    }

    try {
      await this.deleteModule({ id })

      this.$notify({
        type: 'success',
        title: 'Success',
        text: `Deleted module #${id} successfully.`,
      })

      await this.handleGetModules()
    } catch (error) {
      requestCatch(error)
    }
  }

  async handleDeleteModules () {
    if (!confirm(`Confirm to delete selected modules ?`)) {
      return false
    }

    try {
      const modules = this.tableSelected.map(item => item.id)
      await this.deleteModules({ modules })

      this.$notify({
        type: 'success',
        title: 'Success',
        text: `Deleted selected modules successfully.`,
      })

      this.resetSelected()

      await this.handleGetModules()
    } catch (error) {
      requestCatch(error)
    }
  }
}
</script>
