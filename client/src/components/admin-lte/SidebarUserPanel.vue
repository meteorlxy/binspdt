<template>
  <div class="user-panel mt-3 pb-3 mb-3 d-flex">
    <div class="image">
      <slot name="image" />
    </div>

    <div class="info">
      <slot name="info" />
    </div>
  </div>
</template>

<script>
export default {
  name: 'SidebarUserPanel',
}
</script>
