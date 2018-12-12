<template>
  <VContainer
    fluid
    fill-height>
    <VLayout
      align-center
      justify-center>
      <div class="text-xs-center">
        <h1 class="error-page-title">
          404 Not Found
        </h1>

        <p class="error-page-subtitle mt-3">
          <RouterLink :to="{ name: 'home' }">
            Go back home
          </RouterLink>
        </p>
      </div>
    </VLayout>
  </VContainer>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'

@Component
export default class NotFound extends Vue {}
</script>

<style lang="stylus" scoped>
.error-page-title
  font-size 60px
.error-page-subtitle
  font-size 25px
</style>
