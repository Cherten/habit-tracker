import { defineStore } from 'pinia';
import apiClient from '@/services/api';

export const useHabitsStore = defineStore('habits', {
    state: () => ({
        habits: [],
        loading: false,
        error: null
    }),
    actions: {
        async fetchHabits() {
            this.loading = true;
            this.error = null;
            try {
                const response = await apiClient.get('/habits/');
                this.habits = response.data;
            } catch (error) {
                this.error = 'Failed to fetch habits.';
                console.error(error);
            } finally {
                this.loading = false;
            }
        },
        async addHabit(habitData) {
            this.loading = true;
            this.error = null;
            try {
                const response = await apiClient.post('/habits/', habitData);
                this.habits.push(response.data);
            } catch (error) {
                this.error = 'Failed to add habit.';
                console.error(error);
                throw error;
            } finally {
                this.loading = false;
            }
        },
        async deleteHabit(habitId) {
            this.loading = true;
            this.error = null;
            try {
                await apiClient.delete(`/habits/${habitId}/`);
                this.habits = this.habits.filter(h => h.id !== habitId);
            } catch (error) {
                this.error = 'Failed to delete habit.';
                console.error(error);
            } finally {
                this.loading = false;
            }
        },
        async markAsComplete(habitId) {
            try {
                await apiClient.post(`/habits/${habitId}/complete/`);
                // Refresh the list to show the new completion
                await this.fetchHabits(); 
            } catch (error) {
                console.error('Failed to mark as complete:', error);
            }
        },
        async markAsIncomplete(habitId) {
            try {
                await apiClient.post(`/habits/${habitId}/uncomplete/`);
                // Refresh the list to show the removed completion
                await this.fetchHabits();
            } catch (error) {
                console.error('Failed to mark as incomplete:', error);
            }
        }
    }
});
