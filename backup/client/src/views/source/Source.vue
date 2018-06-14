<template>
  <ElContainer>
    <TheSourceAside/>

    <ElMain>
      <transition
        name="el-fade-in-linear"
        mode="out-in">
        <router-view/>
      </transition>
    </ElMain>
  </ElContainer>
</template>

<script>
import TheSourceAside from '@/components/layouts/TheSourceAside'
export default {
  name: 'Source',
  components: {
    TheSourceAside
  },
  created () {
    // this.$store.dispatch('binary/module/get')
  }
}
</script>
