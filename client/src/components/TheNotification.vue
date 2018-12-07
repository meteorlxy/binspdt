<template>
  <VueNotification
    position="top right"
    width="400">
    <template slot="body" slot-scope="{ item: { title = '', type = 'info', text = ''}, close }">
      <Alert
        :type="type"
        @close="close">
        <template slot="title">
          {{ title || type.charAt(0).toUpperCase() + type.slice(1) }}
        </template>

        <span slot="text" v-html="text" />
      </Alert>
    </template>
  </VueNotification>
</template>

<script>
import Alert from '@/components/admin-lte/Alert'

export default {
  name: 'TheNotification',

  components: {
    Alert,
  },
}
</script>

