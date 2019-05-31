<template>
  <VApp>
    <TheNotification />

    <RouterView />
  </VApp>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import TheNotification from '@/components/TheNotification.vue'

@Component({
  components: {
    TheNotification,
  },
})
export default class App extends Vue {
}
</script>

<style lang="stylus">
.v-slider__thumb-label
  background-color: rgb(25, 118, 210) !important
</style>
