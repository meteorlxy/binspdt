<template>
  <div
    v-loading.fullscreen.lock="analysing"
    :element-loading-text="$t('status.analysing')">
    <ModuleSelect v-model="selectedModules"/>

    <p class="hint">{{ $t('binary.analysis.api.select_modules_hint') }}</p>

    <hr>

    <ElForm>
      <ElFormItem :label="$t('binary.analysis.api.call_depth')">
        <ElInputNumber
          :min="0"
          :max="10"
          v-model="k"/>
      </ElFormItem>
    </ElForm>

    <p class="hint">{{ $t('binary.analysis.api.call_depth_hint') }}</p>

    <hr>

    <ElButton
      type="primary"
      :disabled="!selectedModules"
      @click="startAnalysis">
      {{ buttonText }}
    </ElButton>

    <hr>

    <ResultApi :result="result"/>
  </div>
</template>

<script>
import ModuleSelect from '@/components/ModuleSelect'
import ResultApi from '@/components/ResultApi'
export default {
  name: 'AnalysisApi',
  components: {
    ModuleSelect,
    ResultApi
  },
  data () {
    return {
      selectedModules: null,
      k: 2,
      analysing: false,
      result: null
    }
  },
  computed: {
    buttonText () {
      if (this.analysing) {
        return this.$t('status.analysing')
      }
      return this.$t('buttons.submit')
    },
    buttonDisabled () {
      return !this.selectedModules || this.analysing
    }
  },
  methods: {
    async startAnalysis () {
      if (this.buttonDisabled) return
      try {
        this.analysing = true
        const response = await this.$axios.post(this.$api.binary.analysis.api.index(), {
          module_1: this.selectedModules[0],
          module_2: this.selectedModules[1],
          k: this.k
        })
        this.$message({
          type: 'success',
          message: this.$t('binary.analysis.api.messages.analyse_success')
        })
        this.result = response.data.data
      } catch (e) {
        this.$message.error(this.$t('binary.analysis.api.messages.analyse_error', { msg: `${e.description}` }))
      } finally {
        this.analysing = false
      }
    }
  }
}
</script>
