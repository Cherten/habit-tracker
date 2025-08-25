<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth';

const authStore = useAuthStore();
const router = useRouter();
const username = ref('');
const password = ref('');
const error = ref(null);

const handleLogin = async () => {
  try {
    await authStore.login({ username: username.value, password: password.value });
    router.push('/'); // Handle navigation in the component
  } catch (err) {
    error.value = 'Ошибка входа. Проверьте имя пользователя и пароль.';
  }
};
</script>

<template>
  <div class="auth-container">
    <h2>Вход в систему</h2>
    <form @submit.prevent="handleLogin" class="auth-form">
      <div class="form-group">
        <label for="username">Имя пользователя</label>
        <input id="username" v-model="username" type="text" required />
      </div>
      <div class="form-group">
        <label for="password">Пароль</label>
        <input id="password" v-model="password" type="password" required />
      </div>
      <button type="submit">Войти</button>
      <p v-if="error" class="error-message">{{ error }}</p>
    </form>
    <p>
      Нет аккаунта? <router-link to="/register">Зарегистрироваться</router-link>
    </p>
  </div>
</template>
