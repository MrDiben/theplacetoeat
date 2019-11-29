import Vue from "vue";

import BaseHeader from "@/components/base-components/BaseHeader.vue";
import BaseScreen from "@/components/base-components/BaseScreen.vue";
import BaseContent from "@/components/base-components/BaseContent.vue";
import Avatar from "@/components/base-components/Avatar.vue";

export default () => {
  Vue.component(BaseScreen.name, BaseScreen);
  Vue.component(BaseHeader.name, BaseHeader);
  Vue.component(Avatar.name, Avatar);
  Vue.component(BaseContent.name, BaseContent);
};
