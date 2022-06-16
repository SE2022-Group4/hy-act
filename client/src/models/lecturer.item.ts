export interface LecturerItem {
  id: number;
  real_name: string;
  groups: GroupItem[];
  email: string;
  telephone: string;
  majors: MajorItem[];
  departments: DepartmentItem[];
}

interface GroupItem {
  id: number;
  name: string;
}

interface DepartmentItem {
  id: number;
  name: string;
}

interface MajorItem {
  id: number;
  name: string;
}
