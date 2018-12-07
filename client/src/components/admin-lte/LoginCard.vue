<template>
  <div class="card">
    <div class="card-body login-card-body">
      <p class="login-box-msg">
        <slot name="message" />
      </p>

      <slot />
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginCard',
}
</script>

