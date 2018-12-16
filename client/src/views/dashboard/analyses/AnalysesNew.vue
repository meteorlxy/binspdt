<template>
  <VCard class="pt-2">
    <VBtn
      color="grey"
      title="Back To Analyses List"
      :to="{ name: 'dashboard.analyses' }"
      exact
      icon
      flat
      :disabled="isLoading">
      <VIcon>arrow_back</VIcon>
    </VBtn>

    <VStepper
      v-model="currentStep"
      class="elevation-0"
      vertical>
      <!-- Step 1 -->
      <VStepperStep
        step="1"
        :complete="isValid.steps.first">
        <span>Select Two Modules to Analyse</span>

        <span
          v-if="currentStep > 1 && isValid.steps.first"
          class="green--text">
          {{ `[#${steps.first.moduleA.id}] ${steps.first.moduleA.name}  vs.  [#${steps.first.moduleB.id}] ${steps.first.moduleB.name}` }}
        </span>
      </VStepperStep>

      <VStepperContent step="1">
        <VLayout
          row
          wrap>
          <VFlex
            xs12
            md6>
            <ModuleSelect
              v-model="steps.first.moduleA"
              :confirmed.sync="steps.first.confirmedA"
              class="mx-3"
              label="Modules A to analyse"/>
          </VFlex>

          <VFlex
            xs12
            md6>
            <ModuleSelect
              v-model="steps.first.moduleB"
              :confirmed.sync="steps.first.confirmedB"
              class="mx-3"
              label="Modules B to analyse"/>
          </VFlex>

          <VFlex
            class="mt-4 ml-2"
            xs12>
            <VBtn
              color="primary"
              title="Click to next step"
              :disabled="!isValid.steps.first"
              @click="currentStep = 2">
              Continue
            </VBtn>
          </VFlex>
        </VLayout>
      </VStepperContent>

      <!-- Step 2 -->
      <VStepperStep
        step="2"
        :complete="isValid.steps.second">
        <span>Select the Method for Analysis</span>

        <span
          v-if="currentStep > 2 && isValid.steps.second"
          class="green--text">
          {{ `Use method: ${steps.second.method.text}` }}
        </span>
      </VStepperStep>

      <VStepperContent step="2">
        <VLayout
          row
          wrap>
          <VFlex xs12>
            <VSelect
              v-model="steps.second.method"
              label="Analysis Method"
              hint="Select the analysis method"
              persistent-hint
              prepend-icon="assessment"
              :items="methods"
              :item-text="item => item.text"
              :item-value="item => item"/>
          </VFlex>

          <VFlex
            class="mt-4"
            xs12>
            <VBtn
              color="primary"
              title="Click to next step"
              :disabled="!isValid.steps.second"
              @click="currentStep = 3">
              Continue
            </VBtn>

            <VBtn
              title="Click to previous step"
              @click="currentStep = 1">
              Back
            </VBtn>
          </VFlex>
        </VLayout>
      </VStepperContent>

      <!-- Step 3 -->
      <VStepperStep
        step="3"
        :complete="isValid.steps.third">
        <span>Set the Parameters of Analysis Method</span>

        <span
          v-if="currentStep > 3 && isValid.steps.third"
          class="green--text">
          {{ `Params of method: ${steps.second.method.text}` }}
        </span>
      </VStepperStep>

      <VStepperContent step="3">
        <VLayout
          row
          wrap>
          <VFlex xs12>
            <Component
              :is="steps.second.method.paramsComponent"
              v-if="currentStep > 2"
              v-model="steps.third.params"
              :is-valid.sync="steps.third.isValid"/>
          </VFlex>

          <VFlex
            class="mt-4"
            xs12>
            <VBtn
              color="primary"
              title="Click to next step"
              :disabled="!isValid.steps.third"
              @click="currentStep = 4">
              Continue
            </VBtn>

            <VBtn
              title="Click to previous step"
              @click="currentStep = 2">
              Back
            </VBtn>
          </VFlex>
        </VLayout>
      </VStepperContent>

      <!-- Step 4 -->
      <VStepperStep
        step="4"
        :complete="isValid.steps.forth">
        <span>Start a New Analysis</span>
      </VStepperStep>

      <VStepperContent step="4">
        <VLayout
          row
          wrap>
          <VFlex xs12>
            <VTextField
              v-model="steps.forth.description"
              type="text"
              prepend-icon="add_comment"
              label="Description of this analysis"
              hint="Remark on this analysis"
              persistent-hint/>
          </VFlex>

          <VFlex
            class="mt-4"
            xs12>
            <VBtn
              color="success"
              title="Click to submit a new analysis"
              :disabled="!isValid.all"
              @click="handlePostAnalysis">
              <VIcon left>
                check
              </VIcon>
              Submit
            </VBtn>

            <VBtn
              title="Click to previous step"
              @click="currentStep = 3">
              Back
            </VBtn>
          </VFlex>
        </VLayout>
      </VStepperContent>
    </VStepper>
  </VCard>
</template>

<script lang="ts">
import ModuleSelect from './_components/ModuleSelect.vue'
import { Component, Vue } from 'vue-property-decorator'
import { namespace } from 'vuex-class'
import { requestCatch } from '@/utils/catchError'

@Component({
  components: {
    ModuleSelect,
  },
})
export default class AnalysesNew extends Vue {
  @namespace('binary/analyses').State('methods') methods
  @namespace('binary/analyses').Action('postAnalysis') postAnalysis

  currentStep: Number = 1

  steps = {
    first: {
      moduleA: null,
      moduleB: null,
      confirmedA: false,
      confirmedB: false,
    },

    second: {
      method: {
        name: null,
        text: '',
        paramsComponent: '',
      },
    },

    third: {
      isValid: false,
      params: {},
    },

    forth: {
      description: '',
    },
  }

  isLoading: boolean = false

  get isValid () {
    const steps = {
      first: this.steps.first.confirmedA && this.steps.first.confirmedB &&
        this.steps.first.moduleA !== null && this.steps.first.moduleB !== null,
      second: this.methods.some(method => method.name === this.steps.second.method.name),
      third: this.steps.third.isValid,
      forth: this.steps.forth.description !== '',
    }

    const all = !Object.entries(steps).some(item => item[1] === false)

    return {
      steps,
      all,
    }
  }

  get postForm () {
    if (this.isValid.all) {
      return {
        modules: [
          (<any> this.steps.first.moduleA).id,
          (<any> this.steps.first.moduleB).id,
        ],
        method: this.steps.second.method.name,
        params: this.steps.third.params,
        description: this.steps.forth.description,
      }
    } else {
      return false
    }
  }

  async handlePostAnalysis () {
    if (!this.isValid.all) {
      return false
    }

    try {
      this.isLoading = true

      const response = await this.postAnalysis({
        ...this.postForm,
      })

      this.$router.push({
        name: 'dashboard.analyses',
      }, () => {
        this.$notify({
          type: 'success',
          text: `Analysis started. ID: ${response.data.id}`,
        })
      })
    } catch (error) {
      requestCatch(error)
    } finally {
      this.isLoading = false
    }
  }
}
</script>
