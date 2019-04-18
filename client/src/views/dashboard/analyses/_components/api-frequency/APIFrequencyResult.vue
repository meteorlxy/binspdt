<template>
  <VLayout
    row
    wrap
  >
    <VFlex
      xs12
      md4
    >
      <VLayout
        column
        wrap
      >
        <VFlex>
          <VCard>
            <VCardTitle>
              <VBtn
                color="grey"
                title="Back To Analyses List"
                :to="{ name: 'dashboard.analyses' }"
                exact
                icon
                flat
              >
                <VIcon>arrow_back</VIcon>
              </VBtn>

              <VSpacer />

              <VProgressCircular
                v-show="isLoading"
                color="primary"
                indeterminate
              />
            </VCardTitle>

            <VCardText class="text-xs-center">
              <SimilarityCircular :value="overallSimilarity" />
            </VCardText>

            <VCardText class="text-xs-center pb-4">
              <div class="headline">
                Overall Similarity
              </div>

              <div class="grey--text">
                Similarity of the API Frequency birthmark
              </div>
            </VCardText>
          </VCard>
        </VFlex>

        <VFlex>
          <VCard>
            <VCardTitle>
              <div>
                <div class="headline">
                  Parameters
                </div>

                <div class="grey--text">
                  Method: {{ method.text }}
                </div>
              </div>
            </VCardTitle>

            <APIFrequencyParams
              :value="analysis['params']"
              readonly
            />
          </VCard>
        </VFlex>
      </VLayout>
    </VFlex>

    <VFlex
      xs12
      md8
    >
      <VLayout
        row
        wrap
      >
        <VFlex
          xs12
          md6
        >
          <ModuleDetailsCard
            :data="moduleA"
            :fields-hide="['comment', 'exporter', 'import_time']"
          >
            Module A
          </ModuleDetailsCard>
        </VFlex>

        <VFlex
          xs12
          md6
        >
          <ModuleDetailsCard
            :data="moduleB"
            :fields-hide="['comment', 'exporter', 'import_time']"
          >
            Module B
          </ModuleDetailsCard>
        </VFlex>

        <VFlex xs12>
          <VCard>
            <VCardTitle>
              <div>
                <div class="headline">
                  <slot>Matched Functions</slot>
                </div>

                <div class="grey--text">
                  List of functions similarity
                </div>
              </div>
            </VCardTitle>

            <VDataTable
              :headers="tableHeaders"
              :items="tableItems"
              :loading="isLoading"
              :rows-per-page-items="[10, 20, 50, 100]"
            >
              <template v-slot:items="props">
                <tr>
                  <td>{{ props.item.api }}</td>
                  <td>{{ props.item.module_1_frequency }}</td>
                  <td>{{ props.item.module_2_frequency }}</td>
                </tr>
              </template>
            </VDataTable>
          </VCard>
        </VFlex>
      </VLayout>
    </VFlex>
  </VLayout>
</template>

<script lang="ts">
import ModuleDetailsCard from '@/components/dashboard/ModuleDetailsCard.vue'
import SimilarityCircular from '../SimilarityCircular.vue'
import APIFrequencyParams from './APIFrequencyParams.vue'
import { Component, Vue, Prop } from 'vue-property-decorator'
import { namespace } from 'vuex-class'

@Component({
  components: {
    ModuleDetailsCard,
    SimilarityCircular,
    APIFrequencyParams,
  },
})
export default class APIFrequencyResult extends Vue {
  @namespace('binary/modules').Action('getModule') getModule
  @namespace('binary/analyses').State('methods') methods
  @namespace('binary/analyses').State('functionMatchAlgorithms') algorithms

  @Prop({
    type: Object,
    required: true,
  }) analysis!: any

  isLoading: boolean = false

  moduleA: any = {}
  moduleB: any = {}

  overallSimilarity: number = 0

  get method () {
    return this.methods.find(item => item.name === this.analysis['method'])
  }

  get algorithm () {
    return this.algorithms.find(item => item.name === this.analysis['params']['algorithm'])
  }

  get moduleABirthmark () {
    return this.analysis['result']['module_1_birthmark']
  }

  get moduleBBirthmark () {
    return this.analysis['result']['module_2_birthmark']
  }

  get tableItems () {
    const union = Array.from(new Set(Object.keys(this.moduleABirthmark).concat(Object.keys(this.moduleBBirthmark))))
    return union.map((item, index) => ({
      id: index,
      'api': item,
      'module_1_frequency': item in this.moduleABirthmark ? this.moduleABirthmark[item] : 0,
      'module_2_frequency': item in this.moduleBBirthmark ? this.moduleBBirthmark[item] : 0,
    }))
  }

  get tableHeaders () {
    return [
      {
        text: 'API',
        value: 'api',
      },
      {
        text: 'Module A Frequency',
        value: 'module_1_frequency',
      },
      {
        text: 'Module B Frequency',
        value: 'module_2_frequency',
      },
    ]
  }

  async created () {
    await this.handleGetModule()
  }

  mounted () {
    setTimeout(() => {
      this.overallSimilarity = this.analysis['result']['overall_similarity']
    }, 500)
  }

  async handleGetModule () {
    try {
      this.isLoading = true
      const [responseA, responseB] = await Promise.all([
        this.getModule({ id: this.analysis['module_1_id'] }),
        this.getModule({ id: this.analysis['module_2_id'] }),
      ])
      this.moduleA = responseA.data.data
      this.moduleB = responseB.data.data
    } catch (error) {

    } finally {
      this.isLoading = false
    }
  }
}
</script>
