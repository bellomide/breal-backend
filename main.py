from fastapi import FastAPI
from routers import userRouter, paymentRouter, adminRouter, contractorRouter, projectRouter, clientRouter, taskRouter, milestoneRouter, consultationRouter
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins (DEV ONLY)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app = FastAPI()
app.include_router(userRouter.user_router)
app.include_router(contractorRouter.contractor_router)
app.include_router(projectRouter.project_router)
app.include_router(taskRouter.task_router)
app.include_router(consultationRouter.consultation_router)
app.include_router(milestoneRouter.milestone_router)
app.include_router(clientRouter.client_router)
app.include_router(adminRouter.admin_router)
app.include_router(paymentRouter.payment_router)

@app.get('')
def start():
  print("Backend server is running")