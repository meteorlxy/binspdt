<template>
  <VCard>
    <VToolbar
      color="white"
      flat>
      <VToolbarTitle>
        <span>List of Analyses</span>
      </VToolbarTitle>

      <VSpacer/>

      <VBtn
        color="primary"
        title="Create New Analysis"
        :to="{ name: 'dashboard.analyses.new' }"
        :icon="$vuetify.breakpoint.smAndDown">
        <VIcon :left="!$vuetify.breakpoint.smAndDown">
          timeline
        </VIcon>

        <span class="hidden-sm-and-down">
          New Analysis
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
        <VBtn
          slot="activator"
          color="indigo"
          title="Manipulate selected analyses"
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

        <VList>
          <VListTile @click="handleDeleteAnalyses">
            <VListTileAvatar>
              <VIcon>delete</VIcon>
            </VListTileAvatar>

            <VListTileTitle>
              Delete Selected Analyses
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
        @click:append="handleGetAnalyses"
        @keydown.enter="handleGetAnalyses"/>
    </VToolbar>

    <VDataTable
      v-model="tableSelected"
      :headers="tableHeaders"
      :items="tableItems"
      :loading="isLoading"
      :pagination.sync="tablePagination"
      :rows-per-page-items="[10, 25, 50]"
      select-all>
      <template
        slot="items"
        slot-scope="props">
        <td>
          <VCheckbox
            v-model="props.selected"
            primary
            hide-details/>
        </td>

        <td>{{ props.item.id }}</td>

        <td>{{ props.item.description }}</td>

        <td class="hidden-xs-only">
          {{ $helpers.formatDateTime(props.item.created_at) }}
        </td>

        <td>
          <VChip
            class="ma-0"
            :color="getAnalysisStatus(props.item).color"
            outline
            small>
            <VIcon left>
              {{ getAnalysisStatus(props.item).icon }}
            </VIcon>

            {{ getAnalysisStatus(props.item).text }}
          </VChip>
        </td>

        <td>
          <VBtn
            class="ml-0"
            icon
            small
            color="primary"
            title="Inpect this analysis"
            :to="{ name: 'dashboard.analyses.details', params: { id: props.item.id } }"
            :disabled="!props.item.finished_at">
            <VIcon>search</VIcon>
          </VBtn>

          <VBtn
            class="ml-0"
            icon
            small
            color="error"
            title="Remove this analysis"
            @click="handleDeleteAnalysis(props.item.id)">
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
export default class AnalysesIndex extends Vue {
  @namespace('binary/analyses').State('analyses') analyses
  @namespace('binary/analyses').State('isLoading') isLoading
  @namespace('binary/analyses').Action('getAnalyses') getAnalyses
  @namespace('binary/analyses').Action('deleteAnalysis') deleteAnalysis
  @namespace('binary/analyses').Action('deleteAnalyses') deleteAnalyses

  tablePagination: any = {
    page: this.$store.state.binary.analyses.analyses.page,
    rowsPerPage: 25,
    descending: true,
  }

  tableSelected: Array<any> = []

  search: string = ''

  get tableHeaders () {
    return [
      { text: '#', value: 'id' },
      { text: 'Desc.', value: 'description' },
      { text: 'Create Time', value: 'created_at', class: 'hidden-xs-only' },
      { text: 'Status', value: '', sortable: false },
      { text: 'Actions', value: '', sortable: false },
    ]
  }

  get tableItems () {
    return this.analyses.data
  }

  @Watch('tablePagination', { deep: true })
  onTablePaginationChange (val: any) {
    this.handleGetAnalyses()
  }

  created () {
    this.handleGetAnalyses()
  }

  resetSelected () {
    this.tableSelected.splice(0, this.tableSelected.length)
  }

  getAnalysisStatus (analysis) {
    if (analysis.finished_at) {
      return {
        color: 'success',
        text: 'Done',
        icon: 'check',
      }
    } else if (analysis.failed_at) {
      return {
        color: 'red',
        text: 'Failed',
        icon: 'priority_high',
      }
    } else if (analysis.started_at) {
      return {
        color: 'primary',
        text: 'Running',
        icon: 'sync',
      }
    } else {
      return {
        color: 'grey',
        text: 'Pending',
        icon: 'alarm',
      }
    }
  }

  async handleRefresh () {
    this.resetSelected()
    await this.handleGetAnalyses()
  }

  async handleGetAnalyses () {
    const { sortBy, descending, page, rowsPerPage } = this.tablePagination
    await this.getAnalyses({
      page: page,
      perPage: rowsPerPage,
      orderBy: `${descending ? '-' : ''}${sortBy}`,
      search: this.search,
    })
  }

  async handleDeleteAnalysis (id) {
    if (!confirm(`Confirm to delete analysis #${id} ?`)) {
      return false
    }

    try {
      await this.deleteAnalysis({ id })

      this.$notify({
        type: 'success',
        title: 'Success',
        text: `Deleted analysis #${id} successfully.`,
      })

      await this.handleGetAnalyses()
    } catch (error) {
      requestCatch(error)
    }
  }

  async handleDeleteAnalyses () {
    if (!confirm(`Confirm to delete selected analyses ?`)) {
      return false
    }

    try {
      const analyses = this.tableSelected.map(item => item.id)
      await this.deleteAnalyses({ analyses })

      this.$notify({
        type: 'success',
        title: 'Success',
        text: `Deleted selected analyses successfully.`,
      })

      this.resetSelected()

      await this.handleGetAnalyses()
    } catch (error) {
      requestCatch(error)
    }
  }
}
</script>
