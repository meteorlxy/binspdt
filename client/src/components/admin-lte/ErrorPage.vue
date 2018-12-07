<template>
  <div class="error-page">
    <h2 class="headline">
      <slot name="code" />
    </h2>

    <div class="error-content">
      <slot />
    </div>
  </div>
</template>

<script>
export default {
  name: 'ErrorPage',
}
</script>
