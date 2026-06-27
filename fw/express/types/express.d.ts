// Express의 Request 타입을 프로젝트 전역에서 확장
// req.user 같은 커스텀 프로퍼티를 타입 에러 없이 쓰려면 여기에 선언
declare namespace Express {
  interface Request {
    user?: { id: number; name: string };
    step1?: boolean;
    step2?: boolean;
  }
}
