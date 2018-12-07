<template>
  <aside class="main-sidebar sidebar-dark-primary elevation-4">
    <slot name="top" />

    <div class="sidebar">
      <slot name="sub" />

      <nav class="mt-2">
        <ul
          class="nav nav-pills nav-sidebar flex-column"
          role="menu"
          data-widget="treeview"
          data-accordion="false">
          <slot />
        </ul>
      </nav>
    </div>
  </aside>
</template>

<script>
export default {
  name: 'Sidebar',
}
</script>

