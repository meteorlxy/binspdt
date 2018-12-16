<template>
  <PageLoading v-if="isLoading"/>

  <VLayout
    v-else
    row
    wrap>
    <VFlex
      xs12
      md4>
      <VLayout
        column
        wrap>
        <VFlex>
          <ModuleDetailsCard
            :data="moduleData"
            show-all>
            Info
          </ModuleDetailsCard>
        </VFlex>
      </VLayout>
    </VFlex>

    <VFlex
      xs12
      md8>
      <VLayout
        row
        wrap>
        <VFlex xs12>
          <VCard>
            <VCardTitle>
              <div>
                <div class="headline">
                  <slot>Functions</slot>
                </div>

                <div class="grey--text">
                  All functions of this module
                </div>
              </div>
            </VCardTitle>

            <VTreeview
              :items="treeviewItems"
              item-text="text"
              item-key="address"
              :load-children="handleLoadChildren"
              activatable
              open-on-click>
              <template
                slot="prepend"
                slot-scope="{ item }">
                <VIcon>
                  {{ item.icon }}
                </VIcon>
              </template>
            </VTreeview>
          </VCard>
        </VFlex>
      </VLayout>
    </VFlex>
  </VLayout>
</template>

<script lang="ts">
import PageLoading from '@/components/PageLoading.vue'
import ModuleDetailsCard from '@/components/dashboard/ModuleDetailsCard.vue'
import { Component, Vue, Prop } from 'vue-property-decorator'
import { namespace } from 'vuex-class'

@Component({
  components: {
    ModuleDetailsCard,
    PageLoading,
  },
})
export default class APISetResult extends Vue {
  @namespace('binary/modules').Action('getModule') getModule
  @namespace('binary/modules').Action('getModuleFunctions') getModuleFunctions
  @namespace('binary/modules').Action('getFunctionBasicBlocks') getFunctionBasicBlocks
  @namespace('binary/modules').Action('getBasicBlockInstructions') getBasicBlockInstructions

  @Prop({
    type: Number,
    required: true,
  }) id!: number

  isLoading: boolean = false

  moduleData: any = {}
  moduleFunctions: any = []

  treeviewItems: any = []

  created () {
    this.handleGetModule()
    this.handleGetModuleFunctions()
  }

  async handleLoadChildren (item) {
    if (item.type === 'function') {
      return this.handleGetFunctionBasicBlocks(item)
    } else if (item.type === 'basic_block') {
      return this.handleGetBasicBlockInstructions(item)
    }
  }

  async handleGetModule () {
    try {
      this.isLoading = true
      const response = await this.getModule({
        id: this.id,
      })
      this.moduleData = response.data.data
    } catch (error) {

    } finally {
      this.isLoading = false
    }
  }

  async handleGetModuleFunctions () {
    try {
      this.isLoading = true
      const response = await this.getModuleFunctions({
        moduleId: this.id,
      })
      const moduleFunctions = response.data.data
      this.treeviewItems = moduleFunctions.map(item => {
        return {
          address: item['address'],
          text: item['demangled_name'] || item['name'],
          type: 'function',
          icon: 'functions',
          children: (item.type === 0) ? [] : undefined,
        }
      })
    } catch (error) {

    } finally {
      this.isLoading = false
    }
  }

  async handleGetFunctionBasicBlocks (item) {
    try {
      const response = await this.getFunctionBasicBlocks({
        moduleId: this.id,
        functionAddress: item.address,
      })
      const basicBlocks = response.data.data
      item.children = basicBlocks.map(item => {
        return {
          id: item['id'],
          address: item['address'],
          'parent_function': item['parent_function'],
          text: `Basic Block #${item['id']} @ ${this.$helpers.decToHex(item['address'])}`,
          type: 'basic_block',
          icon: 'view_headline',
          children: [],
        }
      })
    } catch (error) {

    } finally {
    }
  }

  async handleGetBasicBlockInstructions (item) {
    try {
      const response = await this.getBasicBlockInstructions({
        moduleId: this.id,
        functionAddress: item['parent_function'],
        basicBlockId: item.id,
      })
      const instructions = response.data.data
      item.children = instructions.map(item => {
        return {
          address: item['address'],
          text: item['mnemonic'],
          type: 'instruction',
          icon: 'remove',
        }
      })
    } catch (error) {

    } finally {
    }
  }
}
</script>
