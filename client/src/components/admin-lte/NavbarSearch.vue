<template>
  <form class="form-inline ml-3">
    <div class="input-group input-group-sm">
      <input
        class="form-control form-control-navbar"
        type="search"
        :placeholder="placeholder"
        :aria-label="placeholder">

      <div class="input-group-append">
        <button
          class="btn btn-navbar"
          type="submit">
          <FaIcon icon="search" />
        </button>
      </div>
    </div>
  </form>
</template>

<script>
export default {
  name: 'NavbarSearch',

  props: {
    placeholder: {
      type: String,
      required: false,
      default: 'Search',
    }
  }
}
</script>