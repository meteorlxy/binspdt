<template>
  <div class="row">
    <div class="col-12 col-sm-6">
      <RouterLink :to="{ name: 'dashboard.modules' }">
        <TheModulesBox />
      </RouterLink>
    </div>

    <div class="col-12 col-sm-6">
      <RouterLink :to="{ name: '' }">
      </RouterLink>
    </div>
  </div>
</template>

<script>
import TheModulesBox from './_components/TheModulesBox'

export default {
  name: 'DashboardHome',

  components: {
    TheModulesBox,
  },
}
</script>

<style lang="scss" scoped>
@import '~@/assets/scss/variables';

.box-link {
  color: $gray-900;
  &:hover {
    color: $gray-700;
  }
}
</style>

