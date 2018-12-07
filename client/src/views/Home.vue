<template>
  <main>
    <RouterLink :to="{ name: 'dashboard' }">Dashboard</RouterLink>
    <RouterLink :to="{ name: 'login' }">Login</RouterLink>
  </main>
</template>

<script>
export default {
  name: 'Home',
}
</script>
