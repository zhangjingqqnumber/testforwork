/**
 * 分座位冒泡排序示例
 * 模拟学生按身高排序来分配座位的场景
 */
public class SeatAllocationBubbleSort {
    
    // 学生类
    static class Student {
        String name;
        int height; // 身高（厘米）
        int seatNumber; // 座位号
        
        public Student(String name, int height) {
            this.name = name;
            this.height = height;
        }
        
        @Override
        public String toString() {
            return name + "(身高:" + height + "cm, 座位:" + seatNumber + ")";
        }
    }
    
    /**
     * 冒泡排序 - 按身高从矮到高排序
     * @param students 学生数组
     */
    public static void bubbleSortByHeight(Student[] students) {
        int n = students.length;
        boolean swapped;
        
        for (int i = 0; i < n - 1; i++) {
            swapped = false;
            
            // 最后 i 个元素已经有序，不需要比较
            for (int j = 0; j < n - 1 - i; j++) {
                // 如果前一个学生比后一个学生高，则交换
                if (students[j].height > students[j + 1].height) {
                    // 交换学生位置
                    Student temp = students[j];
                    students[j] = students[j + 1];
                    students[j + 1] = temp;
                    swapped = true;
                    
                    System.out.println("  交换: " + students[j + 1].name + 
                                     " ↔ " + students[j].name);
                }
            }
            
            // 如果没有发生交换，说明已经有序
            if (!swapped) {
                System.out.println("  → 已经有序，提前结束排序");
                break;
            }
            
            System.out.println("第 " + (i + 1) + " 轮排序完成");
        }
    }
    
    /**
     * 分配座位
     * @param students 已排序的学生数组
     */
    public static void allocateSeats(Student[] students) {
        System.out.println("\n=== 开始分配座位 ===");
        for (int i = 0; i < students.length; i++) {
            students[i].seatNumber = i + 1;
            System.out.println("座位 " + (i + 1) + ": " + students[i]);
        }
    }
    
    /**
     * 打印学生列表
     */
    public static void printStudents(Student[] students, String title) {
        System.out.println("\n" + title);
        System.out.println("=".repeat(50));
        for (Student student : students) {
            System.out.println(student);
        }
        System.out.println("=".repeat(50));
    }
    
    public static void main(String[] args) {
        System.out.println("╔════════════════════════════════════════╗");
        System.out.println("║      分座位系统 - 冒泡排序演示         ║");
        System.out.println("╚════════════════════════════════════════╝");
        
        // 创建学生数组（未排序）
        Student[] students = {
            new Student("张三", 175),
            new Student("李四", 160),
            new Student("王五", 180),
            new Student("赵六", 165),
            new Student("孙七", 170),
            new Student("周八", 155),
            new Student("吴九", 185)
        };
        
        // 打印初始状态
        printStudents(students, "【初始学生列表】");
        
        // 执行冒泡排序
        System.out.println("\n=== 开始冒泡排序（按身高从矮到高）===");
        bubbleSortByHeight(students);
        
        // 打印排序结果
        printStudents(students, "【排序后的学生列表】");
        
        // 分配座位
        allocateSeats(students);
        
        // 最终结果
        System.out.println("\n╔════════════════════════════════════════╗");
        System.out.println("║           座位分配完成！               ║");
        System.out.println("║  原则：矮个子坐前面，高个子坐后面      ║");
        System.out.println("╚════════════════════════════════════════╝");
    }
}
