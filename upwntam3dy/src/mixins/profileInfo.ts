import getFromIdMixin from "./getFromIdMixin";

export default {
    mixins: [getFromIdMixin],
    methods: {

        getCurrentUser(){
            if (this.$route.params.user_id) {
                return this.getUserFromUniversityId(this.$route.params.user_id);
            } else {
                return null; 
            }
        },
    }
  }
  