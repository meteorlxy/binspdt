<template>
  <div>
    <RouterView />

    <TheNotification />
  </div>
</template>

<script>
import TheNotification from '@/components/TheNotification'

export default {
  name: 'App',

  components: {
    TheNotification,
  },
}
</script>
