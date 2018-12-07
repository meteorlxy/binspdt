<template>
  <BoxInfo
    class="box-link"
    bg="info"
    icon="cubes">
    <template slot="text">
      Modules
    </template>

    <template slot="number">
      <FaIcon
        v-show="isLoading"
        icon="spinner"
        spin />

      <span v-show="!isLoading">
        {{ modules.length }}
      </span>
    </template>
  </BoxInfo>
</template>

<script>
import { mapState } from 'vuex'
import BoxInfo from '@/components/admin-lte/BoxInfo'

export default {
  name: 'TheModulesBox',

  components: {
    BoxInfo,
  },

  computed: {
    ...mapState('binary/modules', [
      'isLoading',
      'modules',
    ]),
  },
}
</script>

