<template>
  <div
    v-loading.fullscreen.lock="isImporting"
    :element-loading-text="$t('status.importing')">
    <PageTitle>{{ $t('binary.modules.title') }}</PageTitle>

    <ElRow class="table-tools">
      <ElCol :span="12">
        <ModuleImport v-model="isImporting"/>
      </ElCol>

      <ElCol
        class="text-right"
        :span="12"
      >
        <ElButton
          size="small"
          icon="el-icon-refresh"
          :round="true"
          :loading="isLoading"
          :title="$t('buttons.refresh')"
          @click="get">
          {{ $t('buttons.refresh') }}
        </ElButton>
      </ElCol>
    </ElRow>

    <ElTable
      v-loading="isLoading"
      :data="modules"
      border
      stripe>
      <ElTableColumn type="expand">
        <template slot-scope="props">
          <ElForm label-position="left" inline class="table-details">
            <ElFormItem :label="$t('binary.modules.table.id')">
              <span>{{ props.row.id }}</span>
            </ElFormItem>

            <ElFormItem :label="$t('binary.modules.table.name')">
              <span>{{ props.row.name }}</span>
            </ElFormItem>

            <ElFormItem :label="$t('binary.modules.table.architecture')">
              <span>{{ props.row.architecture }}</span>
            </ElFormItem>

            <ElFormItem :label="$t('binary.modules.table.exporter')">
              <span>{{ props.row.exporter }}</span>
            </ElFormItem>

            <ElFormItem :label="$t('binary.modules.table.base_address')">
              <span>{{ props.row.base_address }}</span>
            </ElFormItem>

            <ElFormItem :label="$t('binary.modules.table.import_time')">
              <span>{{ $helpers.formatDateTime(props.row.import_time) }}</span>
            </ElFormItem>

            <ElFormItem
              class="long"
              :label="$t('binary.modules.table.md5')">
              <span>{{ props.row.md5 }}</span>
            </ElFormItem>

            <ElFormItem
              class="long"
              :label="$t('binary.modules.table.sha1')">
              <span>{{ props.row.sha1 }}</span>
            </ElFormItem>

            <section
              v-show="modules_details.get(props.row.id) || modules_isLoading_details.includes(props.row.id)"
              v-loading="modules_isLoading_details.includes(props.row.id)"
              class="details-section">
              <hr>

              <template v-if="modules_details.get(props.row.id)">
                <ElFormItem
                  class="details"
                  :label="$t('binary.modules.table.functions_count')">
                  <span>{{ modules_details.get(props.row.id).functions_count }}</span>
                </ElFormItem>

                <ElFormItem
                  class="details"
                  :label="$t('binary.modules.table.basic_blocks_count')">
                  <span>{{ modules_details.get(props.row.id).basic_blocks_count }}</span>
                </ElFormItem>

                <ElFormItem
                  class="details"
                  :label="$t('binary.modules.table.instructions_count')">
                  <span>{{ modules_details.get(props.row.id).instructions_count }}</span>
                </ElFormItem>
              </template>
            </section>
          </ElForm>
        </template>
      </ElTableColumn>

      <ElTableColumn
        prop="id"
        :label="$t('binary.modules.table.id')"
        sortable
        width="70"/>

      <ElTableColumn
        prop="name"
        :label="$t('binary.modules.table.name')"
        sortable/>

      <ElTableColumn
        prop="architecture"
        :label="$t('binary.modules.table.architecture')"
        sortable/>

      <ElTableColumn
        prop="import_time"
        :label="$t('binary.modules.table.import_time')"
        :formatter="row => $helpers.formatDateTime(row.import_time)"
        sortable/>

      <ElTableColumn
        :label="$t('binary.modules.table.operation')"
        fixed="right"
        width="140">
        <template slot-scope="scope">
          <ElButton
            size="mini"
            type="primary"
            icon="el-icon-document"
            circle
            :title="$t('buttons.details')"
            :loading="modules_isLoading_details.includes(scope.row.id)"
            :disabled="modules_isDeleting.includes(scope.row.id)"
            @click="handleDetails(scope.row)"/>

          <ElButton
            size="mini"
            type="danger"
            icon="el-icon-delete"
            circle
            :title="$t('buttons.remove')"
            :loading="modules_isDeleting.includes(scope.row.id)"
            :disabled="modules_isLoading_details.includes(scope.row.id)"
            @click="handleDelete(scope.row)"/>
        </template>
      </ElTableColumn>
    </ElTable>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import ModuleImport from '@/components/ModuleImport'
import PageTitle from '@/components/PageTitle'

export default {
  name: 'Modules',
  components: {
    ModuleImport,
    PageTitle
  },
  data () {
    return {
      isImporting: false
    }
  },
  computed: {
    ...mapState('binary/modules', [
      'modules',
      'modules_details',
      'isLoading',
      'modules_isLoading_details',
      'modules_isDeleting'
    ])
  },
  methods: {
    ...mapActions('binary/modules', [
      'get',
      'details',
      'delete'
    ]),

    isModulePending (id) {
      return this.modules_isLoading_details.includes(id) || this.modules_isDeleting.includes(id)
    },

    async handleDetails (row) {
      if (this.isModulePending(row.id)) {
        return false
      }
      await this.details(row.id)
    },

    async handleDelete (row) {
      if (this.isModulePending(row.id)) {
        return false
      }
      try {
        await this.$confirm(
          this.$t('binary.modules.messages.remove_confirm', {
            name: `[${row.id}] ${row.name}`
          }),
          this.$t('messages.title.warning')
        )
        await this.delete(row.id)
      } catch (e) {
        if (e !== 'cancel') {
          throw e
        }
      }
    }
  }
}
</script>
