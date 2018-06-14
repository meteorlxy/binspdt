<template>
  <div>
    <PageTitle>{{ $t('binary.results.title') }}</PageTitle>

    <div class="table-tools">
      <ElButton
        size="small"
        icon="el-icon-refresh"
        :round="true"
        :loading="isLoading"
        :title="$t('buttons.refresh')"
        @click="get">
        {{ $t('buttons.refresh') }}
      </ElButton>
    </div>

    <ElTable
      v-loading="isLoading"
      :data="results"
      border
      stripe>
      <ElTableColumn type="expand">
        <template slot-scope="props">
          <ElForm label-position="left" inline class="table-details">
            <ElFormItem :label="$t('binary.results.table.id')">
              <span>{{ props.row.id }}</span>
            </ElFormItem>

            <ElFormItem :label="$t('binary.results.table.type')">
              <span>{{ props.row.type }}</span>
            </ElFormItem>

            <ElFormItem :label="$t('binary.results.table.module_1')">
              <span>{{ formatModuleName(props.row.module_1_id) }}</span>
            </ElFormItem>

            <ElFormItem :label="$t('binary.results.table.module_2')">
              <span>{{ formatModuleName(props.row.module_2_id) }}</span>
            </ElFormItem>

            <ElFormItem :label="$t('binary.results.table.created_at')">
              <span>{{ $helpers.formatDateTime(props.row.created_at) }}</span>
            </ElFormItem>

            <ElFormItem :label="$t('binary.results.table.finished_at')">
              <span>{{ $helpers.formatDateTime(props.row.finished_at) }}</span>
            </ElFormItem>
          </ElForm>
        </template>
      </ElTableColumn>

      <ElTableColumn
        prop="id"
        :label="$t('binary.results.table.id')"
        sortable
        width="70"/>

      <ElTableColumn
        prop="finished_at"
        :label="$t('binary.results.table.status')"
        sortable
        width="120">
        <template slot-scope="scope">
          <ElTag
            v-if="scope.row.finished_at"
            class="status"
            type="success">
            <i class="el-icon-check"></i>
            <span>{{ $t('binary.results.status.done') }}</span>
          </ElTag>

          <ElTag
            v-else
            class="status"
            type="warning">
            <i class="el-icon-loading"></i>
            <span>{{ $t('binary.results.status.pending') }}</span>
          </ElTag>
        </template>
      </ElTableColumn>

      <ElTableColumn
        prop="created_at"
        :label="$t('binary.results.table.created_at')"
        :formatter="row => $helpers.formatDateTime(row.created_at)"
        sortable
        width="170"/>

      <ElTableColumn
        prop="type"
        :label="$t('binary.results.table.type')"
        sortable
        width="130"/>

      <ElTableColumn
        prop="module_1_id"
        :label="$t('binary.results.table.module_1')"
        :formatter="row => formatModuleName(row.module_1_id)"
        sortable/>

      <ElTableColumn
        prop="module_2_id"
        :label="$t('binary.results.table.module_2')"
        :formatter="row => formatModuleName(row.module_2_id)"
        sortable/>

      <ElTableColumn
        :label="$t('binary.results.table.operation')"
        fixed="right"
        width="140">
        <template slot-scope="scope">
          <ElButton
            size="mini"
            type="primary"
            icon="el-icon-document"
            circle
            :title="$t('buttons.details')"
            :loading="isLoadingDetails === scope.row.id"
            :disabled="!scope.row.finished_at || (isLoadingDetails !== false && isLoadingDetails !== scope.row.id)"
            @click="handleDetails(scope.row)"/>

          <ElButton
            size="mini"
            type="danger"
            icon="el-icon-delete"
            circle
            :title="$t('buttons.remove')"
            :disabled="!scope.row.finished_at || isLoadingDetails && true"
            @click="handleDelete(scope.row)"/>
        </template>
      </ElTableColumn>
    </ElTable>

    <div
      v-show="numPages > 1"
      class="text-center pagination">
      <ElPagination
        layout=" total, sizes, prev, pager, next, jumper"
        :total="numPages"
        :page-size="perPage"
        :page-sizes="[20, 60, 100]"
        @current-change="handlePageChange"
        @size-change="handlePerPageChange"/>
    </div>

    <ElDialog
      class="analysis-result"
      width="90%"
      :title="$t('binary.results.result.title')"
      :visible="showResult"
      :before-close="handleResultClose">
      <component
        :is="currentResultComponent"
        :data="currentResultDetails"/>

      <span slot="footer">
        <ElButton @click="handleResultClose">{{ $t('binary.results.result.close') }}</ElButton>

        <!-- <ElButton type="primary" @click="handleResultSave">{{ $t('binary.results.result.save') }}</ElButton> -->
      </span>
    </ElDialog>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import APIResult from '@/components/results/APIResult'

export default {
  name: 'Results',

  components: {
    APIResult
  },

  data () {
    return {
      showResult: false,
      currentResult: {},
      currentResultDetails: {}
    }
  },

  computed: {
    ...mapState('binary/modules', [
      'modules'
    ]),

    ...mapState('binary/results', [
      'results',
      'count',
      'numPages',
      'page',
      'perPage',
      'isLoading',
      'isLoadingDetails'
    ]),

    currentResultComponent () {
      switch (this.currentResult.type) {
        case 'api':
          return 'APIResult'
        default:
          return {
            render: h => h('span', null, this.$t('status.error'))
          }
      }
    }
  },

  created () {
    this.get({
      page: this.page,
      perPage: this.perPage
    })
  },

  methods: {
    ...mapActions('binary/results', [
      'get',
      'details'
    ]),

    formatModuleName (moduleId) {
      return `[${moduleId}] ${this.modules.find(m => m.id === moduleId).name}`
    },

    async handleDetails (row) {
      this.currentResult = row
      this.currentResultDetails = await this.details(row.id)
      this.showResult = true
    },

    async handleDelete (row) {

    },

    handleResultClose () {
      this.$confirm(this.$t('binary.results.messages.close_confirm'))
        .then(() => {
          this.showResult = false
          this.currentResult = {}
          this.currentResultDetails = {}
        })
        .catch(this.$noop)
    },

    handlePageChange (page) {
      this.get({
        page,
        perPage: this.perPage
      })
    },

    handlePerPageChange (perPage) {
      this.get({
        page: 1,
        perPage
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.pagination {
  padding-top: 15px;
}

.el-tag.status {
  padding-left: 7px;
}
</style>
