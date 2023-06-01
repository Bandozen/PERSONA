<template>
  <tr>
    <td>{{ community.id }}</td>
    <td class="review-title">
      <router-link
      style="text-decoration: none; color: inherit;"
        :to="{
          name: 'CommunityDetailView',
          params: { id: community.id },
        }"
      >
          {{ community.title }}
      </router-link>
    </td>
    <td class="comment-writer">{{ community.user.username }}</td>
    <td class="comment-writer">{{ community.created_at }}</td>
  </tr>
</template>

<script>
export default {
  name: "CommunityListItem",
  props: {
    community: Object,
  },
};
</script>

<style >
.review-title {
  cursor: pointer;
}

</style>
