<script setup>
import { RouterLink, RouterView, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth';

const router = useRouter();

const authStore = useAuthStore();

const handleLogout = () => {
  authStore.logout();
  router.push('/login');
};
</script>

<template>
  <header>
    <div class="wrapper">
      <nav>
        <RouterLink to="/">Главная</RouterLink>
        <template v-if="!authStore.isAuthenticated">
          <RouterLink to="/login">Вход</RouterLink>
          <RouterLink to="/register">Регистрация</RouterLink>
        </template>
        <template v-else>
          <button @click="handleLogout">Выход</button>
        </template>
      </nav>
    </div>
  </header>

  <main>
    <RouterView />
  </main>
</template>

<style scoped>
header {
  background-color: #fff;
  padding: 1rem 2rem;
  border-bottom: 1px solid #eee;
  margin-bottom: 2rem;
}
.wrapper {
    max-width: 800px;
    margin: 0 auto;
}
nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
nav a {
  padding: 0.5rem 1rem;
  text-decoration: none;
  color: #5c67f2;
}
nav a.router-link-exact-active {
  font-weight: bold;
}
nav button {
    background: none;
    border: 1px solid #5c67f2;
    color: #5c67f2;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    cursor: pointer;
    width: auto;
}
nav button:hover {
    background-color: #f4f7f6;
}
</style>
