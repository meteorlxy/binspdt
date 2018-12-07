<template>
  <div class="login-box">
    <slot />
  </div>
</template>

<script>
export default {
  name: 'LoginWrapper',
}
</script>

<style lang="scss">
@import '~@/assets/scss/variables';

.login-box {
  .form-control {
    &:focus {
      box-shadow: none;
      & ~ .input-group-append .input-group-text {
        border-color: $input-focus-border-color;
      }
    }
    
    &.is-valid {
      &:focus {
        box-shadow: none;
      }
      & ~ .input-group-append .input-group-text {
        border-color: $success;
      }
    }

    &.is-invalid {
      &:focus {
        box-shadow: none;
      }
      & ~ .input-group-append .input-group-text {
        border-color: $danger;
      }
    }
  }
  .input-group-append .input-group-text {
    border-left: none;
    transition: $input-transition;
    // Fix boostrap issue temporarily https://github.com/twbs/bootstrap/issues/25110
    border-bottom-right-radius: $border-radius !important;
    border-top-right-radius: $border-radius !important;
  }
}
</style>
