<template>
  <div>
    <h1>Dashboard</h1>
    <template v-if="!isLoading || token">
      <EventCard v-for="event in events" :key="event.id" :event="event" />
    </template>
    <p v-else>Loading events</p>
    <p>
      {{ $store.state.user.token }}
    </p>
  </div>
</template>

<script>
import axios from 'axios';
import EventCard from '../components/EventCard.vue';

export default {
  components: { EventCard },
  data() {
    return {
      isLoading: true,
      events: [],
      token: localStorage.getItem('token'),
    };
  },
  created() {
    axios
      .get('//localhost:3000/dashboard')
      .then(({ data }) => {
        this.events = data.events.events;
        this.isLoading = false;
      })
      .catch(err => {
        console.log('에러 발생 :', err);
      });
  },
};
</script>
