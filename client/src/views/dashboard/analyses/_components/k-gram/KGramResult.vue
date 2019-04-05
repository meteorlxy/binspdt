<template>
  <VLayout
    row
    wrap>
    <VFlex
      xs12
      md4>
      <VLayout
        column
        wrap>
        <VFlex>
          <VCard>
            <VCardTitle>
              <VBtn
                color="grey"
                title="Back To Analyses List"
                :to="{ name: 'dashboard.analyses' }"
                exact
                icon
                flat>
                <VIcon>arrow_back</VIcon>
              </VBtn>

              <VSpacer/>

              <VProgressCircular
                v-show="isLoading"
                color="primary"
                indeterminate/>
            </VCardTitle>

            <VCardText class="text-xs-center">
              <VProgressCircular
                :rotate="360"
                :size="120"
                :width="10"
                :value="similarityAToB * 100"
                :color="similarityAToB > 0.8 ? 'orange' : similarityAToB > 0.4 ? 'blue' : 'teal'">
                {{ $helpers.floatToPercent(similarityAToB) }}
              </VProgressCircular>
            </VCardText>

            <VCardText class="text-xs-center pb-4">
              <div class="headline">
                Module A to B Similarity
              </div>
            </VCardText>

            <VCardText class="text-xs-center">
              <VProgressCircular
                :rotate="360"
                :size="120"
                :width="10"
                :value="similarityBToA * 100"
                :color="similarityBToA > 0.8 ? 'orange' : similarityBToA > 0.4 ? 'blue' : 'teal'">
                {{ $helpers.floatToPercent(similarityBToA) }}
              </VProgressCircular>
            </VCardText>

            <VCardText class="text-xs-center pb-4">
              <div class="headline">
                Module B to A Similarity
              </div>
            </VCardText>

            <VCardText class="text-xs-center pb-4">
              <div class="grey--text">
                Module A K-Grams: {{ analysis['result']['module_1_count'] }}
              </div>

              <div class="grey--text">
                Module B K-Grams: {{ analysis['result']['module_2_count'] }}
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

            <VCardText class="mt-3">
              <VSlider
                :value="analysis['params']['k']"
                readonly
                :max="10"
                :min="1"
                :step="1"
                label="Parameter k"
                ticks="always"
                thumb-label="always"
                hint="Length of subsequence when generating k-grams. [default: 3]"
                persistent-hint>
                <template v-slot:append>
                  <span class="ml-2">
                    {{ analysis['params']['k'] }}
                  </span>
                </template>
              </VSlider>
            </VCardText>
          </VCard>
        </VFlex>
      </VLayout>
    </VFlex>

    <VFlex
      xs12
      md8>
      <VLayout
        row
        wrap>
        <VFlex
          xs12
          md6>
          <ModuleDetailsCard
            :data="moduleA"
            :fields-hide="['comment', 'exporter', 'import_time']">
            Module A
          </ModuleDetailsCard>
        </VFlex>

        <VFlex
          xs12
          md6>
          <ModuleDetailsCard
            :data="moduleB"
            :fields-hide="['comment', 'exporter', 'import_time']">
            Module B
          </ModuleDetailsCard>
        </VFlex>

        <VFlex xs12>
          <VCard>
            <VCardTitle>
              <div>
                <div class="headline">
                  <slot>K-Grams</slot>
                </div>

                <div class="grey--text">
                  List of all k-grams in Module A and B
                </div>
              </div>
            </VCardTitle>

            <VDataTable
              :headers="tableHeaders"
              :items="tableItems"
              :loading="isLoading"
              :rows-per-page-items="[10, 20, 50, 100]">
              <template v-slot:items="props">
                <tr>
                  <td>{{ props.item['k_gram'] }}</td>
                  <td>{{ props.item['in_module_1'] }}</td>
                  <td>{{ props.item['in_module_2'] }}</td>
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
import { Component, Vue, Prop } from 'vue-property-decorator'
import { namespace } from 'vuex-class'

@Component({
  components: {
    ModuleDetailsCard,
  },
})
export default class KGramResult extends Vue {
  @namespace('binary/modules').Action('getModule') getModule
  @namespace('binary/analyses').State('methods') methods

  @Prop({
    type: Object,
    required: true,
  }) analysis!: any

  isLoading: boolean = false

  moduleA: any = {}
  moduleB: any = {}

  similarityAToB: number = 0
  similarityBToA: number = 0

  get method () {
    return this.methods.find(item => item.name === this.analysis['method'])
  }

  get tableItems () {
    const intersection = this.analysis['result']['intersection'].map(item => ({
      k_gram: item,
      in_module_1: true,
      in_module_2: true,
    }))
    const moduleADiff = this.analysis['result']['module_1_diff'].map(item => ({
      k_gram: item,
      in_module_1: true,
      in_module_2: false,
    }))
    const moduleBDiff = this.analysis['result']['module_2_diff'].map(item => ({
      k_gram: item,
      in_module_1: false,
      in_module_2: true,
    }))
    return intersection.concat(moduleADiff, moduleBDiff).map((item, index) => ({
      id: index,
      ...item,
    }))
  }

  get tableHeaders () {
    return [
      {
        text: 'K-Gram',
        value: 'k_gram',
      },
      {
        text: 'Module A',
        value: 'in_module_1',
      },
      {
        text: 'Module B',
        value: 'in_module_2',
      },
    ]
  }

  async created () {
    await this.handleGetModule()
  }

  mounted () {
    setTimeout(() => {
      this.similarityAToB = this.analysis['result']['similarity_1_to_2']
      this.similarityBToA = this.analysis['result']['similarity_2_to_1']
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
