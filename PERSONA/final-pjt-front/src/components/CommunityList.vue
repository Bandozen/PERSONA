<template>
  <div class="community-list">
    <div class="table" v-if="communitys.length > 0">
      <table>
        <thead>
          <tr>
            <th class="num">No.</th>
            <th class="title">Title</th>
            <th class="writer">User</th>
            <th class="date">Date</th>
          </tr>
        </thead>
        <tbody v-if="communitys.length > 0">
          <CommunityListItem
            v-for="community in communitys"
            :key="community.id"
            :community="community"
          />
        </tbody>
        <div v-else>
          <p>작성된 글이 없습니다.</p>
        </div>
      </table>
      <button class="write-btn">
        <router-link style="text-decoration: none; color: inherit;" :to="{ name: 'CommunityCreateView' }">글 작성</router-link>
      </button>
    </div>
    <div v-else>
      <p>작성된 글이 없습니다.</p>
      <button class="write-btn">
        <router-link style="text-decoration: none; color: inherit;" :to="{ name: 'CommunityCreateView' }">글 작성</router-link>
      </button>
    </div>
  </div>
</template>

<script>
import CommunityListItem from "@/components/CommunityListItem";

export default {
  name: "CommunityList",
  components: {
    CommunityListItem,
  },
  computed: {
    communitys() {
      return this.$store.state.communitys;
    },
  },
};
</script>

<style >
.table {
  margin-top: 3rem;
}

.write-btn {
  margin-top: 1rem;
  border: 0.5px solid #4b4a54;
  border-radius: 8%;
  /* width: 4rem; */
  position: relative;
  right: 0;
}

table {
  width: 100%;
  border-top: 2px solid black;
  border-radius: 50%;
  margin: 0;
  position: relative;
  /* left: 50%; */
  /* transform: translate(50%, 0); */
  text-align: center;
}

thead {
  background-color: rgb(233, 235, 233, 0.5);
}

tr {
  border-bottom: 0.5px solid #4b4a54;
}

.num {
  width: 5%;
}

.writer {
  width: 10%;
}

.title {
  width: 70%;
}

.data {
  width: 15%;
}
</style>
