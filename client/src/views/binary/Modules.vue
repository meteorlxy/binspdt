<template>
  <div
    v-loading.fullscreen.lock="importing"
    :element-loading-text="$t('status.importing')">
    <ElRow>
      <ElCol :span="12">
        <ModuleImport v-model="importing"/>
      </ElCol>

      <ElCol
        class="text-right"
        :span="12"
      >
        <ElButton
          size="small"
          type="text"
          :icon="loading ? 'el-icon-loading' : 'el-icon-refresh'"
          :loading="loading"
          @click="get">
          {{ refreshButtonText }}
        </ElButton>
      </ElCol>
    </ElRow>

    <ElTable
      v-loading="loading"
      :data="modules"
      stripe
      style="width: 100%">
      <ElTableColumn
        prop="id"
        :label="$t('binary.modules.table.id')"
        width="70"/>

      <ElTableColumn
        prop="name"
        :label="$t('binary.modules.table.name')"/>

      <ElTableColumn
        prop="architecture"
        :label="$t('binary.modules.table.architecture')"/>

      <ElTableColumn
        prop="import_time"
        :label="$t('binary.modules.table.import_time')"/>

      <ElTableColumn
        :label="$t('binary.modules.table.operation')"
        fixed="right"
        width="140">
        <template slot-scope="scope">
          <ElButton
            size="mini"
            type="danger"
            icon="el-icon-delete"
            @click="handleDelete(scope.row)">
            {{ $t('buttons.remove') }}
          </ElButton>
        </template>
      </ElTableColumn>
    </ElTable>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import ModuleImport from '@/components/ModuleImport'
export default {
  name: 'Modules',
  components: {
    ModuleImport
  },
  data () {
    return {
      importing: false
    }
  },
  computed: {
    ...mapState('binary/module', [
      'modules',
      'loading'
    ]),
    refreshButtonText () {
      if (this.loading) {
        return this.$t('status.loading')
      }
      return this.$t('buttons.refresh')
    }
  },
  methods: {
    ...mapActions('binary/module', [
      'get',
      'delete'
    ]),
    async handleDelete (row) {
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
