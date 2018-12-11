<template>
  <VApp>
    <TheNotification/>

    <RouterView/>
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
