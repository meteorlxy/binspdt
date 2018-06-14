<template>
  <ElContainer>
    <TheBinaryAside/>

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
import TheBinaryAside from '@/components/layouts/TheBinaryAside'
export default {
  name: 'Binary',
  components: {
    TheBinaryAside
  },
  created () {
    this.$store.dispatch('binary/modules/get')
  }
}
</script>
