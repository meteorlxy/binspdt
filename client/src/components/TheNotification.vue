<template>
  <VueNotification
    width="100%"
    :style="style">
    <template
      slot="body"
      slot-scope="{ item: { title = '', type = 'info', text = ''}, close }">
      <VAlert
        class="my-0"
        :type="type"
        :value="true"
        dismissible
        transition="slide-y-transition"
        @input="close">
        <b>
          {{ title || type.charAt(0).toUpperCase() + type.slice(1) }}
        </b>

        <!-- eslint-disable-next-line vue/no-v-html -->
        <span v-html="text"/>
      </VAlert>
    </template>
  </VueNotification>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'

@Component
export default class TheNotification extends Vue {
  get style () {
    if (this.$route === null) {
      return ''
    }
    if (this.$route.name && this.$route.name.startsWith('dashboard')) {
      return {
        top: this.$vuetify.breakpoint.smAndDown ? '56px' : '64px',
      }
    }
  }
}
</script>
