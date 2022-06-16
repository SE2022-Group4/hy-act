export interface UserItem {
  username: string;
  email: string;
  real_name: string;
  groups: UserGroup[];
  majors: MajorGroup[];
  telephone: string;
  departments: string[];
}

interface UserGroup {
  name: string;
}

interface MajorGroup {
  id: number;
  name: string;
}
