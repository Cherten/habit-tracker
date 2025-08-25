import { defineStore } from 'pinia';
import apiClient from '@/services/api';

export const useAuthStore = defineStore('auth', {
    state: () => ({
        accessToken: localStorage.getItem('access_token') || null,
        user: null
    }),
    getters: {
        isAuthenticated: (state) => !!state.accessToken
    },
    actions: {
        async login(credentials) {
            const response = await apiClient.post('/login/', credentials);
            this.accessToken = response.data.token;
            localStorage.setItem('access_token', this.accessToken);
            return response.data; // Return response for the calling component
        },
        async register(userData) {
            await apiClient.post('/register/', userData);
            return await this.login({ username: userData.username, password: userData.password });
        },
        logout() {
            this.accessToken = null;
            this.user = null;
            localStorage.removeItem('access_token');
        }
    }
});
