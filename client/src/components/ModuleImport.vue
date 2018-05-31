<template>
  <ElUpload
    ref="upload"
    :action="$api.binary.modules.import(version)"
    :headers="{ 'X-CSRFToken': $axios.defaults.headers.common['X-CSRFToken'] }"
    :on-progress="onProgress"
    :on-success="onSuccess"
    :on-error="onError"
    :disabled="disabled">
    <ElButton
      size="small"
      type="primary"
      icon="el-icon-upload"
      :loading="disabled">
      {{ buttonText }}
    </ElButton>
  </ElUpload>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  name: 'ModuleImport',
  model: {
    prop: 'importing'
  },
  props: {
    importing: {
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
    ...mapState('binary/module', [
      'loading'
    ]),
    buttonText () {
      if (this.loading) {
        return this.$t('status.loading')
      }
      if (this.importing) {
        return this.$t('status.importing')
      }
      return this.$t('binary.modules.import_button')
    },
    disabled () {
      return this.loading || this.importing
    }
  },
  methods: {
    ...mapActions('binary/module', [
      'get'
    ]),
    onProgress () {
      this.$emit('input', true)
    },
    onSuccess () {
      this.$message({
        message: this.$t('binary.modules.messages.import_success'),
        type: 'success'
      })
      this.get(false)
      this.$emit('input', false)
      this.$refs.upload.clearFiles()
    },
    onError (e) {
      this.$message.error(this.$t('binary.modules.messages.import_error', {
        msg: e.message
      }))
      this.$emit('input', false)
      this.$refs.upload.clearFiles()
    }
  }
}
</script>
