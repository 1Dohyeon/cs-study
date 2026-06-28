import { PrismaClient } from '@prisma/client';

// PrismaClient를 모듈 단위 싱글톤으로 export한다
// 파일을 import할 때마다 new PrismaClient()를 호출하면 DB 커넥션 풀이 중복 생성되므로
// 하나의 인스턴스를 공유한다
export const prisma = new PrismaClient();
