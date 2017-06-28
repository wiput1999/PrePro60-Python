# Description
เนื่องจากพี่ ๆ บางคนลืมประเมินการสอนอาจารย์ ส่งผลให้พี่ ๆ ที่อยากรู้เกรดของตัวเอง ต้องเป็นอันหัวร้อนเป็นอย่างมาก เพราะดูเกรดรายวิชาไม่ได้ จึงขอให้น้องๆ

ช่วยพี่หาเกรดของแต่ละวิชาในเทอมนี้ให้พี่หน่อย

จากภาพด้านบนน้องๆ จะเห็นได้ว่า ถ้าพี่ไม่ประเมินการสอนของอาจารย์ พี่จะไม่สามารถดูเกรดรายวิชาได้เลย 

โดยเกรดจะแสดงเป็นอักษร X ทั้งหมด แทนที่จะเป็น A, B+, B, C+, C, D+, D หรือ F

ถึงแม้พี่จะดูเกรดเป็นรายวิชาไม่ได้ แต่!!!! สังเกตที่แถว Semester ด้านล่างให้ดี ๆ จะเห็นได้ว่าพี่ยังคงสามารถดูเกรดเฉลี่ยของเทอมนั้นๆ ได้อยู่นะ​

และนอกจากนี้ ยังมีตัวช่วยอีกอย่างหนึ่งคือ สามารถดูรายวิชาที่ประกาศเกรดแล้วได้ ในที่นี้คือวิชา FOUNDATION ENGLISH 2 ประกาศมาเป็นวิชาแรก

โดยเกรดเฉลี่ยที่แสดงในภาพด้านบน จะเป็นเกรดเฉลี่ยสะสมของทุกรายวิชาที่อาจารย์ได้ทำการส่งเกรดแล้ว เท่านั้น

และรับประกันว่าจะไม่มีวิชาใดที่ส่งเกรดพร้อมกัน

## หมายเหตุ 

- Section / Sec. คือกลุ่มที่จะไปนั่งเรียน ใครอยู่ Sec เดียวกันก็คือเรียนด้วยกัน ไม่ส่งผลใดๆ ต่อการคิดเกรด

- Credit คือจำนวนหน่วยกิต

- ค่าคะแนน A = 4.0, B+ = 3.5, B = 3.0, C+ = 2.5, C = 2.0, D+ = 1.5, D = 1.0, F = 0.0
 

## อธิบาย Sample Case #1:

พี่ลงทะเบียนเรียนในเทอมนี้ทั้งหมด 2 วิชา ได้แก่ 

- 06016201​ COMPUTER PROGRAMMING​  (3 หน่วยกิต)

- 90201002​ FOUNDATION ENGLISH 2​  (3 หน่วยกิต)

ขณะนี้มี เกรดเฉลี่ยสะสมเป็น 0.00 (เพราะยังไม่มีวิชาใดประกาศเกรด)

ต่อมาวิชารหัส 90201002​​ ประกาศเกรดเป็นวิชาแรก และไปดูในระบบ ปรากฎเกรดเฉลี่ยสะสมรายภาคเรียนเป็น 4.00 ดังนั้นวิชานี้จะต้องได้เกรด A 

ต่อมาวิชารหัส 06016201​ ประกาศเกรดตามหลังมา และไปดูในระบบ ปรากฎเกรดเฉลี่ยสะสมรายภาคเรียนเปลี่ยนเป็น 3.00 ดังนั้นวิชานี้จะต้องได้เกรด C


## Hint
- ใช้เรื่องที่เรียนในสัปดาห์นี้ให้เป็นประโยชน์ อย่างการใช้ dict ร่วมกับ list จะง่ายขึ้นมากกกกกกกกกกกกกก ~ 

# Specification
## Input Specification
```
ทั้งหมด 5N + 1 บรรทัด
บรรทัดแรก: จำนวนเต็ม N เป็นจำนวนวิชาที่ลงทะเบียนเรียนในเทอมนี้
3N บรรทัดต่อมา:

    รหัสวิชา
    ชื่อวิชา
    หน่วยกิต เป็นจำนวนเต็ม
2N บรรทัดต่อมา: 

    รหัสวิชาที่ประกาศเกรด (ตามลำดับการส่งเกรด)
    เกรดเฉลี่ยสะสมหลังการประกาศเกรดในรายวิชานั้น
```
## Output Specification
```
N บรรทัด: แสดงรหัสวิชา ชื่อวิชา และเกรด ของแต่ละวิชา (คั่นด้วย Tab)
เรียงตามรหัสวิชา จากน้อยไปมาก
```

# Sample Case
Input :
```
2
06016201
COMPUTER PROGRAMMING
3
90201002
FOUNDATION ENGLISH 2
3
90201002
4.00
06016201
3.00
```
Output :
```
06016201	COMPUTER PROGRAMMING	C
90201002	FOUNDATION ENGLISH 2	A
```
Input :
```
7
90201002
FOUNDATION ENGLISH 2
3
06016201
MATHEMATICS FOR INFORMATION TECHNOLOGY
3
06016206
COMPUTER PROGRAMMING
3
06016207
COMPUTER SYSTEMS ORGANIZATION AND OPERATING SYSTEM
3
06016208
MULTIMEDIA AND WEB TECHNOLOGY
3
06016278
SPECIAL TOPICS IN INFORMATION TECHNOLOGY 2
3
90010007
THAI GEOSOCIAL DESIGN
3
06016206
4.00
06016207
4.00
06016208
4.00
90010007
4.00
90201002
4.00
06016201
4.00
06016278
4.00
```
Output :
```
06016201	MATHEMATICS FOR INFORMATION TECHNOLOGY	A
06016206	COMPUTER PROGRAMMING	A
06016207	COMPUTER SYSTEMS ORGANIZATION AND OPERATING SYSTEM	A
06016208	MULTIMEDIA AND WEB TECHNOLOGY	A
06016278	SPECIAL TOPICS IN INFORMATION TECHNOLOGY 2	A
90010007	THAI GEOSOCIAL DESIGN	A
90201002	FOUNDATION ENGLISH 2	A
```