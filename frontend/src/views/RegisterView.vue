<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth';

const router = useRouter();

const authStore = useAuthStore();
const username = ref('');
const password = ref('');
const error = ref(null);
const success = ref(false);

const handleRegister = async () => {
  error.value = null;
  success.value = false;
  if(password.value.length < 8) {
    error.value = 'Пароль должен содержать минимум 8 символов.';
    return;
  }
  try {
    await authStore.register({ username: username.value, password: password.value });
    router.push('/'); // Handle navigation in the component
  } catch (err) {
    error.value = 'Ошибка регистрации. Такое имя пользователя уже занято.';
  }
};
</script>

<template>
  <div class="auth-container">
    <h2>Регистрация</h2>
    <form @submit.prevent="handleRegister" class="auth-form">
      <div class="form-group">
        <label for="username">Имя пользователя</label>
        <input id="username" v-model="username" type="text" required />
      </div>
      <div class="form-group">
        <label for="password">Пароль</label>
        <input id="password" v-model="password" type="password" required />
      </div>
      <button type="submit">Зарегистрироваться</button>
      <p v-if="error" class="error-message">{{ error }}</p>
    </form>
    <p>
      Уже есть аккаунт? <router-link to="/login">Войти</router-link>
    </p>
  </div>
</template>
