const database = db.getSiblingDB("college_db");

database.students.drop();

database.students.insertMany([
  { rollNo: 101, name: "Arjun", department: "Computer Science", marks: 89, semester: 5 },
  { rollNo: 102, name: "Priya", department: "Computer Science", marks: 94, semester: 5 },
  { rollNo: 103, name: "Rohan", department: "Electronics", marks: 76, semester: 5 },
  { rollNo: 104, name: "Sneha", department: "Mechanical", marks: 82, semester: 5 },
  { rollNo: 105, name: "Vikram", department: "Computer Science", marks: 67, semester: 5 },
  { rollNo: 106, name: "Kavya", department: "Electronics", marks: 91, semester: 5 },
  { rollNo: 107, name: "Aditya", department: "Civil", marks: 73, semester: 5 },
  { rollNo: 108, name: "Deepika", department: "Computer Science", marks: 88, semester: 5 }
]);

print("Average marks by department");
database.students.aggregate([
  {
    $group: {
      _id: "$department",
      totalStudents: { $sum: 1 },
      averageMarks: { $avg: "$marks" },
      highestMarks: { $max: "$marks" },
      lowestMarks: { $min: "$marks" }
    }
  },
  {
    $project: {
      _id: 0,
      department: "$_id",
      totalStudents: 1,
      averageMarks: { $round: ["$averageMarks", 2] },
      highestMarks: 1,
      lowestMarks: 1
    }
  },
  { $sort: { averageMarks: -1 } }
]).forEach(printjson);

print("Computer Science students with marks greater than or equal to 80");
database.students.aggregate([
  {
    $match: {
      department: "Computer Science",
      marks: { $gte: 80 }
    }
  },
  {
    $project: {
      _id: 0,
      rollNo: 1,
      name: 1,
      department: 1,
      marks: 1
    }
  },
  { $sort: { marks: -1 } }
]).forEach(printjson);
