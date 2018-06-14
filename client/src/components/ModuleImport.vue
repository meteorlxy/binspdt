<template>
  <ElUpload
    ref="upload"
    :action="$api.binary.modules.import(version)"
    :headers="{ 'X-CSRFToken': $axios.defaults.headers.common['X-CSRFToken'] }"
    :on-progress="onProgress"
    :on-success="onSuccess"
    :on-error="onError"
    :disabled="isDisabled">
    <ElButton
      size="small"
      type="warning"
      icon="el-icon-upload"
      :round="true"
      :loading="isDisabled"
      :title="$t('binary.modules.import_button')">
      {{ $t('binary.modules.import_button') }}
    </ElButton>
  </ElUpload>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  name: 'ModuleImport',
  model: {
    prop: 'isImporting',
    event: 'importing'
  },
  props: {
    isImporting: {
      type: Boolean,
      required: false,
      default: false
    }
  },
  data () {
    return {
      version: '6.8'
    }
  },
  computed: {
    ...mapState('binary/modules', [
      'isLoading'
    ]),
    isDisabled () {
      return this.isLoading || this.isImporting
    }
  },
  methods: {
    ...mapActions('binary/modules', [
      'get'
    ]),
    onProgress () {
      this.$emit('importing', true)
    },
    onSuccess () {
      this.$message.success({
        message: this.$t('binary.modules.messages.import_success')
      })
      this.get(false)
      this.$emit('importing', false)
      this.$refs.upload.clearFiles()
    },
    onError (e) {
      this.$message.error({
        message: this.$t('binary.modules.messages.import_error')
      })
      this.$emit('importing', false)
      this.$refs.upload.clearFiles()
    }
  }
}
</script>
