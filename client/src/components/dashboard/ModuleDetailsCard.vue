<template>
  <VCard>
    <VContainer v-if="!hasLoaded">
      <VLayout
        align-center
        justify-center>
        <VProgressCircular
          color="primary"
          indeterminate/>
      </VLayout>
    </VContainer>

    <template v-else>
      <VCardTitle>
        <div>
          <div class="headline">
            <slot>Module</slot>
          </div>

          <div class="grey--text">
            Details of module
          </div>
        </div>
      </VCardTitle>

      <VSlideYTransition appear>
        <VList>
          <VListTile
            v-for="item in displayFields"
            :key="item.name">
            <VListTileContent>
              <VListTileSubTitle>
                {{ item.text }}
              </VListTileSubTitle>

              <VListTileTitle>
                {{ item.value }}
              </VListTileTitle>
            </VListTileContent>
          </VListTile>
        </VList>
      </VSlideYTransition>
    </template>
  </VCard>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator'
import { getFields } from '@/utils/models'
import moduleFields from '@/utils/models/module-fields'

@Component
export default class ModuleDetailsCard extends Vue {
  @Prop({
    type: Object,
    required: true,
  }) data!: any

  @Prop({
    type: Array,
    required: false,
    default: null,
  }) fieldsShow!: Array<string>

  @Prop({
    type: Array,
    required: false,
    default: () => (['comment']),
  }) fieldsHide!: Array<string>

  get hasLoaded () {
    return Object.keys(this.data).length !== 0
  }

  get displayFields () {
    return getFields({
      data: this.data,
      fields: moduleFields,
      fieldsShow: this.fieldsShow,
      fieldsHide: this.fieldsHide,
    })
  }
}
</script>
