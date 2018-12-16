<template>
  <VLayout
    align-center
    justify-center>
    <VProgressCircular
      color="primary"
      indeterminate/>
  </VLayout>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'

@Component
export default class PageLoading extends Vue {
}
</script>
