<template>
  <div
    v-loading.fullscreen.lock="executing"
    :element-loading-text="$t('status.executing')">
    <PageTitle>{{ $t('binary.analysis.api.title') }}</PageTitle>

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
      <p class="hint">{{ $t('binary.analysis.api.call_depth_hint') }}</p>

      <ElFormItem :label="$t('binary.analysis.api.match_algorithm')">
        <ElSelect
          v-model="matchAlgorithm">
          <ElOption
            label="KM"
            value="km">
          </ElOption>
        </ElSelect>
      </ElFormItem>
      <p class="hint">{{ $t('binary.analysis.api.match_algorithm_hint') }}</p>
    </ElForm>

    <hr>

    <ElButton
      type="primary"
      :disabled="!selectedModules"
      @click="startAnalysis">
      {{ buttonText }}
    </ElButton>
  </div>
</template>

<script>
import ModuleSelect from '@/components/ModuleSelect'
import PageTitle from '@/components/PageTitle'

export default {
  name: 'AnalysisApi',
  components: {
    ModuleSelect,
    PageTitle
  },
  data () {
    return {
      selectedModules: null,
      k: 2,
      matchAlgorithm: 'km',
      executing: false
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
      return !this.selectedModules || this.executing
    }
  },
  methods: {
    async startAnalysis () {
      if (this.buttonDisabled) return
      try {
        this.executing = true
        const response = await this.$axios.post(this.$api.binary.analysis.api(), {
          module_1: this.selectedModules[0],
          module_2: this.selectedModules[1],
          k: this.k,
          algorithm: this.matchAlgorithm
        })
        switch (response.data.err) {
          case 1:
            this.$message.warning(this.$t('binary.analysis.messages.pending'))
            break
          case 2:
            this.$message.success(this.$t('binary.analysis.messages.start'))
            break
          default:
            this.$message.success(this.$t('binary.analysis.messages.done'))
        }
      } catch (e) {
        this.$message.error(this.$t('binary.analysis.messages.error'))
      } finally {
        this.executing = false
      }
    }
  }
}
</script>
