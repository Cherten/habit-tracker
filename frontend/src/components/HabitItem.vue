<script setup>
import { useHabitsStore } from '@/stores/habits';
import { computed } from 'vue';

const props = defineProps({
  habit: {
    type: Object,
    required: true
  }
});

const habitsStore = useHabitsStore();
const today = new Date().toISOString().split('T')[0];

const isCompletedToday = computed(() => {
  return props.habit.completions.some(c => c.date === today);
});

const handleDelete = () => {
  if (confirm(`Вы уверены, что хотите удалить привычку "${props.habit.name}"?`)) {
    habitsStore.deleteHabit(props.habit.id);
  }
};

const handleToggleCompletion = () => {
  if (isCompletedToday.value) {
    habitsStore.markAsIncomplete(props.habit.id);
  } else {
    habitsStore.markAsComplete(props.habit.id);
  }
};

</script>

<template>
  <div class="habit-item" :class="{ 'completed': isCompletedToday }">
    <div class="habit-info">
        <h3>{{ habit.name }}</h3>
        <p v-if="habit.description">{{ habit.description }}</p>
    </div>
    <div class="habit-actions">
        <button @click="handleToggleCompletion" class="complete-btn">
            {{ isCompletedToday ? 'Отменить' : 'Выполнено' }}
        </button>
        <button @click="handleDelete" class="delete-btn">Удалить</button>
    </div>
  </div>
</template>

<style scoped>
.habit-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  margin-bottom: 1rem;
  transition: background-color 0.3s ease;
}

.habit-item.completed {
    background-color: #e6fffa;
    border-left: 5px solid #38b2ac;
}

.habit-info h3 {
    margin: 0 0 0.5rem 0;
}
.habit-info p {
    margin: 0;
    font-size: 0.9rem;
    color: #718096;
}

.habit-actions {
    display: flex;
    gap: 0.5rem;
}

.habit-actions button {
    width: auto;
    padding: 0.5rem 1rem;
}

.delete-btn {
    background-color: #e53e3e;
}
.delete-btn:hover {
    background-color: #c53030;
}
</style>
