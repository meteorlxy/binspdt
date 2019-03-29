<template>
  <PageLoading v-if="isLoading"/>

  <Component
    :is="method.resultComponent"
    v-else
    :analysis="analysis"/>
</template>

<script lang="ts">
import PageLoading from '@/components/PageLoading.vue'
import APISetResult from './_components/api-set/APISetResult.vue'
import { Component, Vue, Prop } from 'vue-property-decorator'
import { namespace } from 'vuex-class'

@Component({
  components: {
    PageLoading,
  },
})
export default class AnalysesDetails extends Vue {
  @namespace('binary/analyses').State('methods') methods
  @namespace('binary/analyses').Action('getAnalysis') getAnalysis

  @Prop({
    type: Number,
    required: true,
  }) id!: number

  analysis: any = null
  isLoading: boolean = false

  get method () {
    if (this.analysis === null) {
      return false
    }

    return this.methods.find(item => item.name === this.analysis.method) || false
  }

  created () {
    this.handleGetAnalysis()
  }

  async handleGetAnalysis () {
    try {
      this.isLoading = true
      const response = await this.getAnalysis({ id: this.id })
      this.analysis = response.data.data
    } catch (error) {
      // Show the notice
      this.$notify({
        type: 'error',
        title: 'Error',
        text: `Failed to load the analyse result.`,
      })
      this.$router.go(-1)
    } finally {
      this.isLoading = false
    }
  }
}
</script>
