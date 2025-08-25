<script setup>
import { onMounted, ref } from 'vue';
import { useHabitsStore } from '@/stores/habits';
import HabitItem from '@/components/HabitItem.vue';

const habitsStore = useHabitsStore();
const newHabitName = ref('');
const newHabitDescription = ref('');
const showForm = ref(false);

onMounted(() => {
  habitsStore.fetchHabits();
});

const handleAddHabit = async () => {
    if(!newHabitName.value) return;
    await habitsStore.addHabit({
        name: newHabitName.value,
        description: newHabitDescription.value
    });
    newHabitName.value = '';
    newHabitDescription.value = '';
    showForm.value = false;
}
</script>

<template>
  <div class="habits-container">
    <header class="habits-header">
        <h1>Мои привычки</h1>
        <button @click="showForm = !showForm" class="add-habit-btn">
            {{ showForm ? 'Отмена' : '+ Добавить привычку' }}
        </button>
    </header>

    <form v-if="showForm" @submit.prevent="handleAddHabit" class="add-habit-form">
        <div class="form-group">
            <input v-model="newHabitName" type="text" placeholder="Название привычки (например, Читать книги)" required>
        </div>
        <div class="form-group">
            <textarea v-model="newHabitDescription" placeholder="Описание (необязательно)"></textarea>
        </div>
        <button type="submit">Добавить привычку</button>
    </form>
    
    <div v-if="habitsStore.loading" class="loading">Загрузка привычек...</div>
    <div v-if="habitsStore.error" class="error-message">{{ habitsStore.error }}</div>
    
    <div v-if="!habitsStore.loading && habitsStore.habits.length > 0" class="habits-list">
        <HabitItem v-for="habit in habitsStore.habits" :key="habit.id" :habit="habit" />
    </div>

    <div v-if="!habitsStore.loading && habitsStore.habits.length === 0 && !showForm" class="no-habits">
        <p>У вас пока нет привычек. Нажмите "+ Добавить привычку" чтобы создать первую!</p>
    </div>
  </div>
</template>

<style scoped>
.habits-container {
    /* ... */
}
.habits-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;
}
.add-habit-btn {
    width: auto;
}
.add-habit-form {
    margin-bottom: 2rem;
    padding: 1.5rem;
    border: 1px solid #ddd;
    border-radius: 8px;
    background-color: #f9fafb;
}

.add-habit-form .form-group {
  margin-bottom: 1rem;
}

.add-habit-form input,
.add-habit-form textarea {
  width: 100%;
  padding: 0.75rem;
  box-sizing: border-box;
  border: 1px solid #ccc;
  border-radius: 4px;
}
.no-habits {
    text-align: center;
    padding: 2rem;
    color: #718096;
}
</style>
